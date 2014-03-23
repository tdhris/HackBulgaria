from time import time
import os
from datetime import datetime


def take(command):
    order = command.split(" ")
    name = order[1]
    price = order[2]
    print("Taking order from %s for %s" % (name, price))
    return order


def save(orders, number_saves):
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')

    #add the name of the current save to the archive with the index [i] of the save in front of it
    if number_saves == 1:
        key = "w"
    else:
        key = "a"

    archive = open("archive.txt", key)
    archive.write('[' + str(number_saves) + ']' + ' ' + stamp + '\n')
    archive.close()

    #create a file with the current date and time and save the curret order in it
    file = open(stamp + '.txt', "w")
    for client in orders.keys():
        file.write(client + " - " + orders[client] + '\n')
    file.close()
    return True


def print_status(orders):
    for client in orders.keys():
        print(client + " - " + orders[client])
    return True


def load(command):
    order = command.split(" ")
    index = '[' + order[1] + ']'
    stamp = ''
    file = open("archive.txt", "r")
    for line in file:
        if line.startswith(index):
            stamp = line[4:].rstrip("\n")
    file.close()

    print("Loading orders " + stamp)
    file = open(stamp + ".txt", "r")
    content = []
    for line in file:
        content += line.rstrip("\n").split(" - ")
    file.close()
    names = content[::2]
    prices = content[1::2]
    orders = dict(zip(names, prices))
    return orders


def print_list():
    if os.path.exists("archive.txt"):
        file = open("archive.txt", "r")
        print(file.read())
        file.close()
        return True
    return False


def main():
    file = open("archive.txt", "w").close()
    file_with_commands = open("menu_commands.txt", "r")
    print(file_with_commands.read())
    command = input("Enter your command> ")
    orders = {}
    unsaved_load_pressed_once = False
    number_saves = 0
    is_order_saved = False
    list_printed = False

    while command != 'finish':
        if command.startswith('take'):
            order = take(command)
            name = order[1]
            price = order[2]
            orders[name] = price
            is_order_saved = False

        elif command == 'status':
            print_status(orders)

        elif command == 'save':
            is_order_saved = True
            list_printed = False
            number_saves += 1
            save(orders, number_saves)

        elif command == 'list':
            print_list()
            list_printed = True

        elif command.startswith('load'):
            if list_printed is False:
                print("Use list command before loading")

            elif is_order_saved is False and unsaved_load_pressed_once is False:
                unsaved_load_pressed_once = True
                print("You have not saved the current order.\n If you wish to discard it, type load <number> again.")

            elif (is_order_saved is False and unsaved_load_pressed_once is True) or is_order_saved is True:
                orders.clear()
                orders = load(command)

            else:
                print("Unknown command!!!")

        command = input("Enter your command> ")

    else:
        if is_order_saved is False:
            file = open("unsaved_order.txt", "r")
            print(file.read())
            file.close()

        command = input("Enter your command> ")
        if command == 'save':
            number_saves += 1
            save(orders, number_saves)
            print("Your order has been saved. Goodbye!")
        elif command == 'finish':
            print("Finishing order. Goodbye!")


if __name__ == '__main__':
    main()
