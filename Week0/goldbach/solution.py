def isPrime(number):
	for i in range(2,number-1):
		if number % i == 0:
			return False
	return True

def get_first_n_primes(n):
	primes = []
	numbers = range(2, n)
	for number in numbers:
		if isPrime(number):
			primes.append(number)

	return primes


def goldbach(n):
	goldbach = []
	primes = get_first_n_primes(n)
	for first_prime in primes:
		for second_prime in primes:
			if first_prime + second_prime == n and first_prime <= n//2:
				goldbach.append((first_prime, second_prime))
	return goldbach


def main():
	print(goldbach(4))
	print(goldbach(6))
	print(goldbach(8))
	print(goldbach(10))
	print(goldbach(100))


if __name__ == '__main__':
	main()