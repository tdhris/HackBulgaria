import unittest
from solution import is_decreasing

class DecrasingTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual(True, is_decreasing([5,4,3,2,1]))
		self.assertEqual(False, is_decreasing([1,2,3]))
		self.assertEqual(True, is_decreasing([100, 50, 20]))
		self.assertEqual(False, is_decreasing([1,1,1,1]))


if __name__ == '__main__':
	unittest.main()