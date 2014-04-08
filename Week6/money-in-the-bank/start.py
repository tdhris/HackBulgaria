import sql_manager
from getpass import getpass
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import string
from random import randrange

ASCII = string.ascii_letters


def main_menu():
    print("Welcome to our bank service. You are not logged in. \n\
           Please register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            email = input("Enter your email: ")

            if sql_manager.register(username, password, email):
                print("Registration Successfull")
            else:
                print("Your password is not strong enough.")

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")

            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            change_password(logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def change_password(logged_user):
    user_email = logged_user.get_email()
    random_string = generate_random_string()
    unique_hash_code = sql_manager.hash_function(random_string)

    send_email(user_email, unique_hash_code)
    code = input("Enter the code you received at {0}".format(user_email + ": "))
    if code == unique_hash_code:
        new_pass = getpass("Enter your new password: ")

        if sql_manager.strong_password(logged_user.get_username(), new_pass):
            sql_manager.change_pass(new_pass, logged_user)
            print("Password Successfully Changed")
        else:
            print("Your password is not strong enough.")

        sql_manager.change_pass(new_pass, logged_user)
    else:
        print("Sorry, wrong code")


def send_email(user_email, unique_hash_code):
    smtp_host = "smtp.gmail.com"
    login, passw = 'ttestov64', 'Blah$$1234'

    message = MIMEText(unique_hash_code, 'plain', 'utf-8')
    message['From'] = login
    message['To'] = user_email
    message['Subject'] = Header('changing your password', 'utf-8')

    host = smtplib.SMTP(smtp_host, 587, timeout=10)
    try:
        host.starttls()
        host.login(login, passw)
        host.sendmail(message['From'], message['To'], message.as_string())
    finally:
        host.quit()


def generate_random_string():
    upper_bound = len(ASCII)
    string_length = 15
    random_string = ''

    for i in range(string_length):
        random_int = randrange(upper_bound)
        random_string += ASCII[random_int]
    return random_string


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
