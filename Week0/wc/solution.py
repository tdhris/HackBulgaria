import sys

def count_chars(filename):
	file = open(filename, "r")
	content = file.read()[:-1]
	file.close()
	count = 0
	for letter in content:
		count+=1
	return count

def count_words(filename):
	file = open(filename, "r")
	content = file.read().split()
	file.close()
	count = 0
	for word in content:
		count+=1
	return count

def count_lines(filename):
	file = open(filename, "r")
	count = 0
	for line in file:
		count +=1
	file.close()
	return count

def main():
	if len(sys.argv) > 1:
		command = sys.argv[1]
		filename = sys.argv[2]

		if command == 'chars':
			count = count_chars(filename)
		elif command == 'words':
			count = count_words(filename)
		elif command == 'lines':
			count = count_lines(filename)
		else:
			print("Error!!")

		print(count)


if __name__ == '__main__':
	main()