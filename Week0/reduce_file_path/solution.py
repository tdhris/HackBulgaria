def remove_double_slash(string):
	while string.find('//') != -1:
		string = string.replace('//', '/')

	return string


def reduce_file_path(path):
	# /smth//smthg/./fggh/../

	path = remove_double_slash(path)

	#dividing path into subpaths
	subpaths = []
	start = 0
	end = 0

	while end != len(path)-1:
		start = end
		end = path.find('/', start+1)
		if end == -1:
			subpaths.append(path[start+1:])
			break
		subpaths.append(path[start+1:end])


	#reducing path
	if len(subpaths) == 0 or len(subpaths) == 1:
		return '/'
	
	else:
		for subpath in reversed(subpaths):
			if subpath == '..':
				i = subpaths.index(subpath)
				subpaths = subpaths[:i-1]+subpaths[i+1:]

			if subpath == '.':
				subpaths.remove(subpath)


	if len(subpaths) == 0:
		return '/'

	path = ''

	for subpath in subpaths:
			path += '/' + subpath

	return path

