import os

def ext(path, file_ext):
	count = 0

	if not file_ext.startswith('.'):
		return 0

	os.chdir(path)
	for file in os.listdir():
		if file.endswith(file_ext):
			count += 1

	return count

