def list_to_number(digits):
	d = 10**(len(digits) - 1)
	num = 0
	for digit in digits:
		num += digit * d
		d = d//10

	return num