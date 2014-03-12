import unittest
from solution import number_of_digits
from solution import is_int_palindrome
from solution import get_digits

class PalindromTests(unittest.TestCase):

	def test_number_of_digits(self):
		self.assertEqual(3, number_of_digits(123))
		self.assertEqual(5, number_of_digits(98765))

	def test_get_digits(self):
		self.assertEqual([3, 2, 1], get_digits(123))

	def test_palindrom(self):
		self.assertEqual(False, is_int_palindrome(42))
		self.assertEqual(True, is_int_palindrome(1))
		self.assertEqual(True, is_int_palindrome(100001))
		self.assertEqual(True, is_int_palindrome(999))
		self.assertEqual(False, is_int_palindrome(123))


if __name__ == '__main__':
	unittest.main()