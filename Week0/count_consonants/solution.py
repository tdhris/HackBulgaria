def count_consonants(str):
	vowels = 'bcdfghjklmnpqrstvwxz'
	count = 0
	for vowel in vowels:
		i = 0
		while i < len(str):
			if vowel == str[i] or vowel.upper() == str[i]:
				count += 1
			i+=1

	return count

