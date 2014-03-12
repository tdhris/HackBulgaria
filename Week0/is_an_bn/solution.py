def countLetter(word, letter):
	count = 0
	for i in range(len(word)):
		if word[i] == letter:
			count+=1

	return count

def is_an_bn(word):
	count_a = countLetter(word, 'a')
	count_b = countLetter(word, 'b')

	return count_a == count_b and word.find('ba') == -1
	

