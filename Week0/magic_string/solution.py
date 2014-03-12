def magic_string(string):
	length = len(string)
	moves = 0

	for i in range(length//2):
		if string[i] == '<':
			moves+=1
		if string[length-1 -i] == '>':
			moves+=1

		i+=1

	return moves


