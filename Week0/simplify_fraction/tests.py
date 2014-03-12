import unittest
from solution import simplify_fraction

class SimplifyFractionTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual((1,3), simplify_fraction((3,9)))

	def test_2(self):
		self.assertEqual((1,7), simplify_fraction((1,7)))

	def test_3(self):
		self.assertEqual((2, 5), simplify_fraction((4,10)))

	def test_4(self):
		self.assertEqual((3,22), simplify_fraction((63,462)))

	def test_5(self):
		self.assertEqual((5,7), simplify_fraction((50,70)))


if __name__ == '__main__':
	unittest.main()