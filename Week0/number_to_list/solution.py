def number_of_digits(n):
	divisor = 1
	num = 0
	while n // divisor != 0:
		num +=1
		divisor *=10

	return num


def number_to_list(n):
	list_of_num = []
	divisor = 1
	while n//divisor != 0:
		num = (n//divisor)%10
		list_of_num.insert(0,num)
		divisor *= 10

	return list_of_num
