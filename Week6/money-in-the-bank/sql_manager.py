import hashlib
import time
from string import ascii_letters
import sqlite3
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()
# five_minutes_sec = 5 * 60


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                email TEXT,
                failed_attempts INTEGER DEFAULT 0,
                time_blocked INTEGER DEFAULT 0)'''

    cursor.execute(create_query)


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

    select_query = "SELECT id, username, password, balance, message, email,\
                    failed_attempts, time_blocked FROM clients WHERE username = ?"


    cursor.execute(select_query, (username,))
    user = cursor.fetchone()

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

    client = Client(user_id, username, balance, message, email, failed_attempts, time_blocked)

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


def failed_login(username):
    select_query = "SELECT failed_attempts, time_blocked FROM clients WHERE username = ?"
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
    update_query = "UPDATE clients SET time_blocked = 0 and failed_attempts = 0\
                    WHERE username = ?"
    cursor.execute(update_query, (username,))
    conn.commit()


def hash_function(password):
    hash_function = hashlib.sha1()
    hash_function.update(password.encode('utf-8'))
    return hash_function.hexdigest()


def strong_password(username, password):
    """
    More then 8 symbols
    Must have capital letters, and numbers and special symbol
    Username is not in the password
    """
    if not eight_symbols(password):
        return False
    elif not special_symbols(password):
        return False
    elif username in password:
        return False
    else:
        return True


def eight_symbols(password):
    count = 0
    for letter in password:
        count += 1
        if count >= 8:
            return True
    return False


def special_symbols(password):
    capital_letters_in_password = False
    numbers_in_password = False
    special_symbol_in_password = False
    special_symbols = "][?/<~#` !@$%^&*()+=}|:;',\">{"

    for symbol in password:
        if symbol in ascii_letters.upper():
            capital_letters_in_password = True
        if symbol.isdigit():
            numbers_in_password = True
        if symbol in special_symbols:
            special_symbol_in_password = True

    return capital_letters_in_password and numbers_in_password and special_symbol_in_password
