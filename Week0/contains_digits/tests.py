import unittest
from solution import contains_digits

class ContainsDigitsTests(unittest.TestCase):

	def test_1(self):
		self.assertEqual(True, contains_digits(402123, [0, 3, 4]))

	def test_2(self):
		self.assertEqual(False, contains_digits(666, [6,4]))

	def test_3(self):
		self.assertEqual(False, contains_digits(123456789, [1,2,3,0]))

	def test_4(self):
		self.assertEqual(True, contains_digits(456, []))

	def test_5(self):
		self.assertEqual(True, contains_digits(4567, [4,7]))

if __name__ == '__main__':
	unittest.main()