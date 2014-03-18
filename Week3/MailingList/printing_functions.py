def greet_user():
	print("Welcome to SuperCool MailList.\nType <<help>>, to see a list of commands.")


def print_list_of_commands():
	file = open("list_of_commands.txt", "r")
	list_of_commands = file.read()
	file.close()
	print(list_of_commands)


def bad_input_warning():
	print("Invalid input. Type <<help>>, to see a list of commands.")


def print_file_content(filename):
	file = open(filename, "r")
	content = file.read()
	file.close()
	print(content)


def print_elements_of_list(list):
	for element in list:
		print(element)


if __name__ == '__main__':
	main()