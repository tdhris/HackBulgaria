def count_numbers(numbers):

	for number in numbers:
		i = numbers.index(number)
		sub_numbers = numbers[:i] + numbers[i+1:]
		for sub_number in sub_numbers:
			if sub_number < number:
				new_number = number // sub_number
				if new_number != 0 and new_number not in numbers:
						numbers.append(new_number)


	count = len(numbers)
	return count

