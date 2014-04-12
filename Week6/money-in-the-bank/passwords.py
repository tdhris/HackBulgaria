import sql_manager
from client_email import send_email
import time
from random import randrange
from getpass import getpass
from string import ascii_letters


ASCII = ascii_letters


def reset_password(username):
    user = sql_manager.get_client_by_username(username)
    user_email = user.get_email()
    user_id = user.get_id()

    changepass, code_generated = sql_manager.get_changepass_details(user_id)
    currenttime = int(time.time())
    five_minutes = 5 * 60

    code = input("Enter the code you received at {0}".format(
        user_email + ": "))
    if code == changepass and currenttime < code_generated + five_minutes:
        new_pass = getpass("Enter your new password: ")

        if sql_manager.strong_password(username, new_pass):
            sql_manager.change_pass(new_pass, user)
            print("Password Successfully Changed")
        else:
            print("Your password is not strong enough.")

        sql_manager.change_pass(new_pass, user)
    elif currenttime > code_generated + five_minutes:
        print("Sorry. You've entered a code that's no longer valid")
    else:
        print("Sorry, wrong code")


def change_password(logged_user):
    new_pass = getpass("Enter your new password: ")
    sql_manager.change_pass(new_pass, logged_user)
    print('Password Successfully Changed')


def send_changepass_email(username):
    user = sql_manager.get_client_by_username(username)
    random_string = generate_random_string()
    unique_hash_code = sql_manager.hash_function(random_string)
    sql_manager.save_changepass_code(user.get_id(), unique_hash_code)

    send_email(user.get_email(),
               unique_hash_code,
               'changing your email')


def generate_random_string(length=15):
    upper_bound = len(ASCII)
    random_string = ''

    for i in range(length):
        random_int = randrange(upper_bound)
        random_string += ASCII[random_int]
    return random_string


def send_tan(user):
    '''
    interface that handles the process of seinding TAN codes
    which allows users to make transactions
    '''
    tan_codes = []
    length = 32
    for i in range(10):
        tan_code = generate_random_string(length)
        tan_codes.append(tan_code)
    sql_manager.save_tan_codes(user.get_id(), tan_codes)

    user.tans = tan_codes

    user_email = user.get_email()
    message = 'tan codes'
    send_email(user_email, '\n'.join(tan_codes), message)

    print("Ten new tan codes have been sent to your email")


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
        if symbol in ASCII.upper():
            capital_letters_in_password = True
        if symbol.isdigit():
            numbers_in_password = True
        if symbol in special_symbols:
            special_symbol_in_password = True

    return capital_letters_in_password and\
        numbers_in_password and\
        special_symbol_in_password
