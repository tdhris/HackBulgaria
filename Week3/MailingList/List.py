import json

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


def merge_lists(first_list, second_list, name_new_list):
	merged_list = List(name_new_list)
	merged_list_filename = get_valid_filename(merged_list.list_name)
	on_both_lists = get_people_from_list(first_list) + get_people_from_list(second_list)
	unique_subscribers = get_unique_subscribers(on_both_lists)
	for person in unique_subscribers:
		add_person_to_list_file(person, merged_list_filename)


def get_people_from_list(list_index):
	list_filename = get_list_from_archive(list_index)
	list_people = []
	file =  open(list_filename, "r")
	for line in file:
		list_people.append(get_person_from_list_entry(line))
	return list_people


def get_person_from_list_entry(list_entry):
	personal_info = [info.rstrip('\n') for info in list_entry.split()[1:] if info != '-']
	name, email = '', ''
	for info in personal_info:
		if '@' not in info:
			name += info + ' '
		else:
			email = info
	subscriber = Person(name.rstrip('\n'), email)
	return subscriber


def get_unique_subscribers(on_both_lists):
	unique_subscribers = []
	for person in on_both_lists:
	 	if email_not_in_list(person.email, unique_subscribers):
	 		unique_subscribers.append(person)
	return unique_subscribers


def email_not_in_list(email, list):
	not_in_list = True
	for person in list:
		if email == person.email:
			not_in_list = False
			break
	return not_in_list

def dictionary_with_people(list_index):
	people = get_people_from_list(list_index)
	people_on_list = []
	for person in people:
		personal_info = {}
		personal_info["name: "] = person.name
		personal_info["email: "] = person.email
		people_on_list.append(personal_info)
	return people_on_list


def export(list_index):
	people_on_list = dictionary_with_people(list_index)
	print(people_on_list)
	list_filename = get_list_from_archive(list_index)
	json_filename = list_filename.replace(".txt", ".json")
	file = open(json_filename, "w").close()
	with open(json_filename, "a") as file:
		file.write(json.dumps(people_on_list, file, sort_keys=True, indent=4))