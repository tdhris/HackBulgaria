import os
import sys

def ext(file_ext):
	if not file_ext.startswith("."):
		return 0

	working_directory = os.getcwd()
	count = 0
	for file in os.listdir(working_directory):
		if file.endswith(file_ext):
			count += 1
	return count



