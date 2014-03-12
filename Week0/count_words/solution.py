def count_words(arr):
	c_words = {}

	for word in arr:
		count = 1
		i = arr.index(word)
		for w in arr[i+1:]:
			if word == w:
				count+=1

		isPresent = False

		for w2 in c_words:
			if word == w2:
				isPresent = True

		if isPresent == False:
			c_words[word] = count

	return c_words

