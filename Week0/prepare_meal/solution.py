def largest_power(number, divisor):
	power = 0
	while number%divisor == 0:
		power+=1
		number = number // divisor

	return power

def prepare_meal(number):
	if number % 3 == 0 and number % 5 == 0:
		n3 = largest_power(number, 3)
		n5 = largest_power(number,5)
		answer = 'spam ' * n3 + "and" + ' eggs' * n5
		return answer
	elif number % 3 == 0:
		n = largest_power(number, 3)
		answer = "spam " * n
		return answer.rstrip(" ")
	elif number % 5 == 0:
		n = largest_power(number, 5)
		answer = "eggs " * n
		return answer.rstrip(" ")
	else:
		return ''


