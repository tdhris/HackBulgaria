import unittest
from solution import sort_fractions

class SortFractions(unittest.TestCase):

	def test_1(self):
		self.assertEqual([(1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2)]))

	def test_2(self):
		self.assertEqual([(1, 3), (1, 2), (2, 3)], sort_fractions([(2, 3), (1, 2), (1, 3)]))

	def test_3(self):
		self.assertEqual([(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)], sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))



if __name__ == '__main__':
	unittest.main()