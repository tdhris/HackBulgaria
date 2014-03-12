import unittest
from solution import sum_of_min_and_max


class SumMinMaxTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual(10, sum_of_min_and_max([1,2,3,4,5,6,8,9]))

	def test_2(self):
		self.assertEqual(90, sum_of_min_and_max([-10,5,10,100]))

	def test_3(self):
		self.assertEqual(2, sum_of_min_and_max([1]))

if __name__ == '__main__':
	unittest.main()