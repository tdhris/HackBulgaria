class Person:
	def __init__(self, name, email):
		self.name = name
		self.email = email


class List:
	archive_filename = 'archive.txt'

	def __init__(self, list_name):
		self.list_name = list_name
		self.create_list_file()
		self.add_list_to_archive()

	def create_list_file(self):
		list_filename = get_valid_filename(self.list_name)
		open(list_filename, "w").close()

	def add_list_to_archive(self):
		index = get_index_of_new_line(self.archive_filename)
		identifier = get_identifier(index)
		entry = set_entry([identifier, self.list_name])
		write_to_file(self.archive_filename, entry, "a")


#helper functions
def create_archive():
	open("archive.txt", "w").close()


def get_valid_filename(list_name):
	name = remove_spaces(list_name)
	return add_txt_extention(name)


def remove_spaces(name):
	return name.replace(' ', '_')


def add_txt_extention(filename):
	return filename + '.txt'


def remove_txt_extention(filename):
	return filename.rstrip('.txt')


def get_index_of_new_line(filename):
	file = open(filename, "r")
	index = 0
	for line in file:
		index += 1
	file.close()
	return index + 1


def get_identifier(index):
	return '[' + str(index) + ']'


def set_entry(list_of_elements):
	separator = ' '
	entry = separator.join(list_of_elements) + '\n'
	return entry


def get_arguments(command, number_of_arguments):
	arguments = [arg.rstrip('\n') for arg in command.split(' ', number_of_arguments)[1:]]
	if len(arguments) == 1:
		return str(arguments[0])
	else:
		return arguments


def get_list_from_archive(list_index, mode = "f"):
	identifier = get_identifier(list_index)
	archive = open("archive.txt", "r")
	for line in archive:
		if line.startswith(identifier):
			list_name = get_arguments(line, 1)
			filename = get_valid_filename(list_name)
			break
	if mode == "f":
		return filename
	elif mode == "l":
		return list_name


def add_person_to_list_file(new_person, list_name):
	index = get_index_of_new_line(list_name)
	identifier = get_identifier(index)
	info = [identifier, new_person.name, '-', new_person. email]
	entry = set_entry(info)
	write_to_file(list_name, entry, "a")


def write_to_file(filename, entry, mode):
	file = open(filename, mode)
	file.write(entry)
	file.close()


def get_list_name_from_command(command):
	default_number_arguments = 1
	list_index = get_arguments(command, default_number_arguments)
	list_name = get_list_from_archive(list_index)
	return list_name


def is_in_list(filename, goal):
	file = open(filename, "r")
	for line in file:
		if goal in line:
			file.close()
			return True
	file.close()
	return False


def find_email(email):
	mailing_lists = []
	list_count = get_index_of_new_line("archive.txt")
	for i in range(1, list_count):
	 	list_name = get_list_from_archive(i, "l")
	 	list_filename = get_list_from_archive(i)
	 	if is_in_list(list_filename, email):
	 		mailing_lists.append(list_name)
	return mailing_lists
