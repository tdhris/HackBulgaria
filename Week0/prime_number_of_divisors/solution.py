def prime_number_of_divisors(n):
	if n == 1:
		return True

	num_of_divisors = 2
	i = 2
	while i < n:
		if n%i == 0:
			num_of_divisors += 1
		i += 1

	j = 2
	while j < num_of_divisors:
		if num_of_divisors%j == 0:
			return False
		j +=1
	return True
