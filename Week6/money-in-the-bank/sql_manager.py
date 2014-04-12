import hashlib
import time
from passwords import strong_password
import sqlite3
from Client import Client

conn = sqlite3.connect("bank2.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                email TEXT,
                changepass_code TEXT,
                changepass_generated INTEGER DEFAULT 0,
                failed_attempts INTEGER DEFAULT 0,
                time_blocked INTEGER DEFAULT 0) '''

    cursor.execute(create_query)

    create_tan_table = '''create table if not exists
            tans(user_id INTEGER, tan_code,
                foreign key(user_id) references clients(id))'''

    cursor.execute(create_tan_table)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    new_pass = hash_function(new_pass)
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def save_changepass_code(user_id, code):
    currenttime = int(time.time())
    update_sql = 'UPDATE clients SET changepass_code = ?,\
                  changepass_generated = ?\
                  WHERE id = ?'
    cursor.execute(update_sql, (code, currenttime, user_id))
    conn.commit()


def get_changepass_code(user_id):
    query = 'SELECT changepass_code, changepass_generated\
             FROM clients WHERE id = ?'
    cursor.execute(query, (user_id,))
    unparsed_info = cursor.fetchone()

    if not unparsed_info:
        return False

    changepass = unparsed_info[0]
    changepass_generated = unparsed_info[1]
    return (changepass, changepass_generated)


def register(username, password, email):
    if not strong_password(username, password):
        return False

    password = hash_function(password)

    insert_sql = "insert into clients (username, password, email)\
                  values (?, ?, ?)"

    cursor.execute(insert_sql, (username, password, email))
    conn.commit()
    return True


def login(username, provided_password):
    provided_password = hash_function(provided_password)
    client, password = get_client_by_username(username)

    if password != provided_password:
        failed_login(username)
        return False

    if client.is_blocked:
        print("User is blocked.")
        return False

    elif not client.is_blocked:
        if client.get_failed_attempts() >= 5:
            unblock_client(username)

    return client


def get_client_by_username(username):
    select_query = "SELECT id, username, password, balance, message, email,\
                    failed_attempts, time_blocked FROM clients\
                    WHERE username = ?"

    cursor.execute(select_query, (username,))
    user = cursor.fetchone()
    #if no user with this username exists, return false
    if not user:
        return False

    user_id = user[0]
    username = user[1]
    password = user[2]
    balance = user[3]
    message = user[4]
    email = user[5]
    failed_attempts = user[6]
    time_blocked = user[7]

    client = Client(user_id, username, balance, message, email,
                    failed_attempts, time_blocked)
    client.tans = get_tans(user_id)
    return (client, password)


def get_tans(user_id):
    select_query = 'SELECT tan_code FROM tans WHERE user_id = ?'
    cursor.execute(select_query, (user_id,))
    tans = [tan[0] for tan in cursor.fetchall()]
    return tans


def remove_used_tan(user_id, tan):
    delete_query = 'DELETE FROM tans WHERE tan_code = ? AND user_id = ?'
    cursor.execute(delete_query, (tan, user_id))
    conn.commit()


def failed_login(username):
    select_query = "SELECT failed_attempts, time_blocked\
                    FROM clients WHERE username = ?"
    cursor.execute(select_query, (username,))
    failure_info = cursor.fetchone()

    failed_attempts = failure_info[0]
    time_blocked = failure_info[1]

    if failed_attempts == 5 and time_blocked == 0:
        print("5 failed attempts. Blocking user ".format(username))
        block_user(username)
        return
    if failed_attempts >= 5 and time_blocked != 0:
        return

    update_query = "UPDATE clients SET failed_attempts = failed_attempts + 1\
                    WHERE username = ?"
    cursor.execute(update_query, (username,))
    conn.commit()


def block_user(username):
    time_blocked = int(time.time())
    update_query = "UPDATE clients SET time_blocked = ? WHERE username = ?"
    cursor.execute(update_query, (time_blocked, username))
    conn.commit()


def unblock_client(username):
    update_query = "UPDATE clients\
                    SET time_blocked = 0 and failed_attempts = 0\
                    WHERE username = ?"
    cursor.execute(update_query, (username,))
    conn.commit()


def hash_function(password):
    hash_function = hashlib.sha1()
    hash_function.update(password.encode('utf-8'))
    return hash_function.hexdigest()


def deposit_money(user_id, amount):
    update_query = "UPDATE clients SET balance = balance + ? WHERE id = ?"
    cursor.execute(update_query, (amount, user_id))
    conn.commit()


def withdraw_money(user_id, amount):
    update_query = "UPDATE clients SET balance = balance - ? WHERE id = ?"
    cursor.execute(update_query, (amount, user_id))
    conn.commit()


def save_tan_codes(user_id, tan_codes):
    insert_query = "INSERT INTO tans VALUES (?, ?)"
    for tan_code in tan_codes:
        cursor.execute(insert_query, (user_id, tan_code))
    conn.commit()
