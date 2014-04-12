import sql_manager
from getpass import getpass
from passwords import change_password, send_tan


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
            print("Your balance is: $" + str(logged_user.get_balance()))

        elif command == 'changepass':
            change_password(logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'show-balance':
            print(logged_user.get_balance())

        elif command == 'withdraw':
            amount = int(input("Enter amount: "))
            tan = input("Enter tan code: ")
            if amount < logged_user.get_balance():
                if tan in logged_user.tans:
                    logged_user.delete_tan(tan)
                    sql_manager.remove_used_tan(logged_user.get_id(), tan)
                    sql_manager.withdraw_money(logged_user.get_id(), amount)
                    logged_user.withdraw_money(amount)
                    print("Successfull Transaction. You have: {0}".format(logged_user.get_balance()))
                else:
                    print("Sorry. Wrong or old tan code.")
            else:
                print("Sorry. You're too poor to make this transaction")

        elif command == 'deposit':
            amount = int(input("Enter amount: "))
            tan = input("Enter tan code: ")
            if tan in logged_user.tans:
                logged_user.delete_tan(tan)
                sql_manager.remove_used_tan(logged_user.get_id(), tan)
                logged_user.deposit_money(amount)
                sql_manager.deposit_money(logged_user.get_id(), amount)
                print("Successfull Transaction. You have: {0}".format(logged_user.get_balance()))
            else:
                print("Sorry, wrong or already used tan code")

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")

        elif command == 'get-tan':
            tan_count = len(logged_user.tans)
            print(tan_count)
            if not tan_count:
                send_tan(logged_user)
            else:
                print("You have {0} remainig TAN codes to use".format(tan_count))

        elif command == 'exit':
            return


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
