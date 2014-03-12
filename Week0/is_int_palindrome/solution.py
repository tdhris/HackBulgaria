def number_of_digits(n):
	number_of_digits = 0
	while n > 0:
		number_of_digits += 1
		n = n // 10
	return number_of_digits

def get_digits(n):
	digits = []
	while n > 0:
		digits.append(n%10)
		n = n // 10
	return digits

def strip_first_and_last_digit(n):
	digits = get_digits(n)
	reduced_number = ''
	for digit in digits[1:-1]:
		reduced_number += str(digit)
	return int(reduced_number)

def is_int_palindrome(n):
	if number_of_digits(n) <= 1:
		return True
	digits = get_digits(n)
	
	return digits[0] == digits[-1] and is_int_palindrome(strip_first_and_last_digit(n))