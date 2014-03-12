import unittest
from solution import sum_of_digits

class SumDigitsTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual(43, sum_of_digits(1325132435356))

	def test_2(self):
		self.assertEqual(6, sum_of_digits(123))

	def test_3(self):
		self.assertEqual(6, sum_of_digits(6))

	def test_4(self):
		self.assertEqual(1, sum_of_digits(-10))

	def test_5(self):
		self.assertEqual(10, sum_of_digits(-1234))


if __name__ == '__main__':
	unittest.main()