def remove_double_slash(string):
	while '//' in string:
		string = string.replace('//', '/')
	return string

def get_subpaths(path):
	if path.endswith('/') and path.startswith('/'):
		return path[1:-1].split('/')
	else:
		return path[1:].split('/')


def reduce_file_path(path):
	# /smth//smthg/./fggh/../

	list_of_subpaths = [subpath for subpath in get_subpaths(path) if subpath != '']
	subpaths = ['/']

	#reducing path
	if len(list_of_subpaths) == 0 or path == "/":
		return '/'

	else:
		for subpath in list_of_subpaths:
			if subpath == '..' and len(subpaths) > 0:
				subpaths.pop()

			elif subpath == '.':
				continue
			else:
				subpaths.append(subpath)

	if len(subpaths) == 0:
		return '/'

	path = '/'.join(subpaths)
	path = remove_double_slash(path)

	return path