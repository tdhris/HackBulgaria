import unittest
from solution import number_to_list

class NumberToListTests(unittest.TestCase):

	def test_1(self):
		self.assertEqual([1, 2, 3], number_to_list(123))

	def test_2(self):
		self.assertEqual([9, 9, 9, 9, 9], number_to_list(99999))

	def test_3(self):
		self.assertEqual([1, 2, 3, 0, 2, 3], number_to_list(123023))

if __name__ == '__main__':
	unittest.main()