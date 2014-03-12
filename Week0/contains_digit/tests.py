import unittest
from solution import contains_digit

class ContainsDigitTest(unittest.TestCase):

	def test_true(self):
		self.assertTrue(contains_digit(123, 1))
		self.assertTrue(contains_digit(987654, 9))
		self.assertTrue(contains_digit(1000, 0))
		self.assertTrue(contains_digit(42, 2))

	def test_false(self):
		self.assertFalse(contains_digit(12346789, 5))
		self.assertFalse(contains_digit(123, 4))

if __name__ == '__main__':
	unittest.main()