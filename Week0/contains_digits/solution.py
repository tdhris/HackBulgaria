def contains_digits(num, digits):
	if len(digits) == 0:
		return True
	else:
		count = 0
		for digit in digits:
			d = 1
			while (num//d)!=0:
				if (num // d)%10 == digit:
					count +=1
					break
				d *= 10
				
		return count == len(digits)

def main():
	print(contains_digits(402123, [0, 3, 4]))
	print(contains_digits(666, [6,4]))
	print(contains_digits(123456789, [1,2,3,0]))
	print(contains_digits(456, []))
	print(contains_digits(4567, [4,7]))

if __name__ == '__main__':
	main()