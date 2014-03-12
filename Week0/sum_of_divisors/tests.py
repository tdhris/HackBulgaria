import unittest
from solution import sum_of_divisors

class SumDivisorsTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual(15, sum_of_divisors(8))

	def test_2(self):
		self.assertEqual(8, sum_of_divisors(7))

	def test_3(self):
		self.assertEqual(1, sum_of_divisors(1))

	def test_4(self):
		self.assertEqual(2340, sum_of_divisors(1000))



if __name__ == '__main__':
	unittest.main()