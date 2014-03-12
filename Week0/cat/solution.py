import sys

def cat(file_name):
   	file = open(file_name, "r")
   	print(file.read())
   	file.close()

def main():
    cat(sys.argv[1])

if __name__ == '__main__':
    main()
