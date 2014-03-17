import sys

def specify(filename):
	file = open(filename, "r")
	contents = file.read().replace("\t", "    ")
	file.close()
	file = open(filename, "w")
	file.write(contents)
	file.close()

def main():
	specify(sys.argv[1])
	
if __name__ == '__main__':
	main()