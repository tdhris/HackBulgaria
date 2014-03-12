import unittest
from solution import prime_number_of_divisors

class PrimeNumberDivisorsTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual(True, prime_number_of_divisors(7))

	def test_2(self):
		self.assertEqual(False, prime_number_of_divisors(8))

	def test_3(self):
		self.assertEqual(True, prime_number_of_divisors(9))

if __name__ == '__main__':
	unittest.main()