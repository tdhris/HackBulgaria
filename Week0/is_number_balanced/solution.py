def number_of_digits(n):
	divisor = 1
	num = 0
	while n // divisor != 0:
		num +=1
		divisor *=10

	return num

def is_number_balanced(n):
	if number_of_digits(n) == 1:
		return True
	else:
		sum_left = 0
		sum_right = 0
		i = 1
		right_divisor = 1
		left_divisor = 10**(number_of_digits(n) - 1)
		while i <= number_of_digits(n) // 2:
			sum_right += (n // right_divisor)%10
			sum_left += (n // left_divisor)%10
			left_divisor /= 10
			right_divisor *= 10
			i+=1

		if sum_left == sum_right:
			return True
		else:
			return False