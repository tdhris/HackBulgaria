import sys
import os
from time import time
from datetime import datetime

def count_lines(filename):
	count = 0
	file = open(filename, "r")
	for line in file:
		count +=1
	file.close()

	return count


def create():
	ts = time()
	stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
	file_name = "attendance_" + stamp + ".txt"

	if os.path.exists(file_name) == False:
		file = open(file_name, "w")
		file.close()
		index = count_lines("archive.txt") + 1
		archive = open("archive.txt", "a")
		archive.write('[' + str(index) + '] - ' + file_name + '\n')
		archive.close()

		print("New file created and loaded: " + file_name)

	else:
		print("You already have a file for today it is: " + file_name)


def main():

	file = open("menuhelp.txt", "r")
	print(file.read())
	file.close()

	ts = time()
	stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
	filename = "attendance_" + stamp + ".txt"

	command = ''
	while command != 'finish':

		command = input("Enter your command > ")

		if command == 'create':
			create()

		elif command.startswith('add') == True:
			
			is_listed = False
			is_attending = False
			com = command.split(" ")
			name = com[1]

			file_students = open("list_students.txt", "r")
			for student in file_students:
				if student.rstrip('\n') == name:
					is_listed = True

			if is_listed == False:
				print ("What the fck are you doing in my class?")

			else: 

				if os.path.exists(filename) == True:
					file = open(filename, "r")
					for student in file:
						if student.rstrip('\n') == name:
							is_attending = True
							print("Student already added to the list")

					if is_attending == False:
						file.close()
						file = open(filename, "a")
						file.write(name + '\n')
					file.close()

			
				else:
					print("You must create an attendance file for today before you mark attendance")

		elif command == 'list':
			file = open("archive.txt", "r")
			print(file.read())
			file.close()

		elif command.startswith('load'):
			com = command.split(" ")
			index = '[' + com[1] + '] - '

			file = open('archive.txt', "r")
			for line in file:
				if line.startswith(index):
					n = line.split(' - ')
					filename = n[1].rstrip('\n')

		elif command == 'status':
			file = open(filename, "r")
			print(file.read())
			file.close()

		elif command == 'statistics':
			archive = open('archive.txt', 'r')
			for line in archive:
				date = line[17:27]
				
				com = line.rstrip('\n').split(' - ')
				file_name = com[1]
				student_count = count_lines(file_name)

				print (date + ' - ' + str(student_count))
		else:
			file = open("menuhelp.txt", "r")
			print(file.read())
			file.close()




if __name__ == '__main__':
	main()