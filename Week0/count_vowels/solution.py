def count_vowels(str):
	vowels = 'aeiouy'
	count = 0
	for vowel in vowels:
		i = 0
		while i < len(str):
			if vowel == str[i] or vowel.upper() == str[i]:
				count += 1
			i+=1

	return count


def main():
	print(count_vowels("Python"))
	print(count_vowels("Theistareykjarbunga"))
	print(count_vowels("grrrrgh!"))
	print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
	print(count_vowels("A nice day to code!"))
	print(count_vowels("Aaaa noooooOOO"))
	print(count_vowels("aaaa noooooooo"))

if __name__ == '__main__':
	main()