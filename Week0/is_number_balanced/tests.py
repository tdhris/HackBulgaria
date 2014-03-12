import unittest
from solution import is_number_balanced


class BalancedTests(unittest.TestCase):

	def test_balanced(self):
		self.assertTrue(is_number_balanced(9))
		self.assertTrue(is_number_balanced(11))
		self.assertTrue(is_number_balanced(121))
		self.assertTrue(is_number_balanced(4518))
		self.assertTrue(is_number_balanced(1238033))

	def test_not_balanced(self):
		self.assertFalse(is_number_balanced(13))
		self.assertFalse(is_number_balanced(28471))

if __name__ == '__main__':
	unittest.main()