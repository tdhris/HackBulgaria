import sys

def concat_files(filenames = sys.argv[1:]):
	for filename in filenames:
		file = open(filename, "r")
		mega = open("MEGATRON.txt", "a")
		mega.write("".join(file.read()))
		file.close()

def main():
	filenames = sys.argv[1:]
	concat_files(filenames)

if __name__ == '__main__':
	main()