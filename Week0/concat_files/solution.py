import sys

def concat_files(filenames = sys.argv[1:]):
	for filename in filenames:
		file = open(filename, "r")
		mega = open("MEGATRON.txt", "a")
		mega.write("".join(file.read()))
		mega.close()
		file.close()