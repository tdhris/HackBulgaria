def isPrime(n):
	if n == 1:
		return False

	i = 2
	while i < n:
		if n%i == 0:
			return False
		i+=1

	return True

def getPrimes(n):
	primes = []
	if n == 1:
		return primes

	i = 2
	while i < n:
		if n%i == 0 and isPrime(i) == True:
			primes += [i]
		i+=1

	return sorted(primes)

def prime_factorization(n):
	factorization = []

	if n == 1:
		return [(1,0)]

	if isPrime(n) == True:
		return [(n, 1)]
	
	primes = getPrimes(n)
	for prime in primes:
		power = 0
		while n % prime == 0:
			power+=1
			n /= prime
		factor = (prime, power)
		factorization.append(factor)

	return factorization

