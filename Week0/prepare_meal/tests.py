import unittest
from solution import prepare_meal

class PrepareMealTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual("eggs", prepare_meal(5))

	def test_2(self):
		self.assertEqual("spam", prepare_meal(3))

	def test_3(self):
		self.assertEqual("spam spam spam", prepare_meal(27))

	def test_4(self):
		self.assertEqual("spam and eggs", prepare_meal(15))

	def test_5(self):
		self.assertEqual("spam spam and eggs", prepare_meal(45))

	def test_6(self):
		self.assertEqual("", prepare_meal(7))

if __name__ == '__main__':
	unittest.main()