def sum_of_divisors(n):
	i = 1
	sum = 0
	while i <= n:
		if n%i == 0:
			sum += i
		i += 1
	return sum


def main():
	print(sum_of_divisors(8))
	print(sum_of_divisors(7))
	print(sum_of_divisors(1))
	print(sum_of_divisors(1000))


if __name__ == '__main__':
	main()