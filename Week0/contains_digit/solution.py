def contains_digit(num, digit):
	d = 1
	while num // d != 0:
		if (num // d)%10 == digit:
			return True
		d *= 10
	return False