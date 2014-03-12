def unique_words_count(arr):
	unique_words = len(arr)
	
	repeated_words = {}

	for word in arr:
		count = 1
		i = arr.index(word)
		for w in arr[i+1:]:
			if word == w:
				count+=1

		isPresent = False

		for w2 in repeated_words:
			if word == w2:
				isPresent = True

		if isPresent == False:
			repeated_words[word] = count

	unique_words = len(repeated_words)

	return unique_words

