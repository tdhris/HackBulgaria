import sys

def cat(argv):
	if len(argv) > 1:
		file_names = []
		for arg in argv[1:]:
			file_names.append(arg)

		for file_name in file_names:
			file = open(file_name, "r")
			print(file.read())
			file.close()

def main():
	cat(sys.argv)

if __name__ == '__main__':
    main()