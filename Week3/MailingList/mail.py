import printing_functions
import List


def process_input(command):
	if command == 'exit':
		printing_functions.greet_user()

	elif command == 'help':
		printing_functions.print_list_of_commands()

	elif command == 'show_lists':
		archive = "archive.txt"
		printing_functions.print_file_content(archive)

	elif command.startswith('show_list '):
		list_name = List.get_list_name_from_command(command)
		printing_functions.print_file_content(list_name)

	elif command.startswith('add '):
		list_name = List.get_list_name_from_command(command)
		new_person = add_person()
		List.add_person_to_list_file(new_person, list_name)

	elif command.startswith('create '):
		list_name = List.get_arguments(command, 1)
		new_list = List.List(list_name)

	elif command.startswith('search_email'):
		email = List.get_arguments(command, 1)
		active_mailing_lists = List.find_email(email)
		printing_functions.print_elements_of_list(active_mailing_lists)

	elif command.startswith('merge_lists'):
		arguments = List.get_arguments(command, 3)
		first_list, second_list, name_new_list = arguments[0], arguments[1], arguments[2]
		List.merge_lists(first_list, second_list, name_new_list)

	elif command.startswith('export'):
		list_index = List.get_arguments(command, 1)
		List.export(list_index)
		
	else:
		printing_functions.bad_input_warning()


def take_input():
	command = input(">> ")
	return command

def add_person():
	name = input("Enter name >> ")
	email = input("Enter email >>")
	new_person = List.Person(name, email)
	return new_person

def main():
	printing_functions.greet_user()
	command = take_input()

	while True:
		process_input(command)
		command = take_input()


if __name__ == '__main__':
	main()