def sum_of_digits (x):
	if x < 0:
		x *= -1

	digits = []

	while x > 0:
		digits.append(x % 10)
		x = x // 10

	return sum(digits)
