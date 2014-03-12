import unittest
from solution import goldbach

class GoldbachTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual([(2,2)], goldbach(4))

	def test_2(self):
		self.assertEqual([(3,3)], goldbach(6))

	def test_3(self):
		self.assertEqual([(3,5)], goldbach(8))

	def test_4(self):
		self.assertEqual([(3,7), (5,5)], goldbach(10))
		
	def test_5(self):
		self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)], goldbach(100))



if __name__ == '__main__':
	unittest.main()
