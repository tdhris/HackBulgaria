import unittest
from solution import what_is_my_sign

class SignTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual("Leo", what_is_my_sign(5, 8))

	def test_2(self):
		self.assertEqual("Aquarius", what_is_my_sign(29, 1))

	def test_3(self):
		self.assertEqual("Cancer", what_is_my_sign(30, 6))

	def test_4(self):
		self.assertEqual("Gemini", what_is_my_sign(31, 5))

	def test_5(self):
		self.assertEqual("Aquarius", what_is_my_sign(2, 2))

	def test_6(self):
		self.assertEqual("Taurus", what_is_my_sign(8, 5))

	def test_7(self):
		self.assertEqual("Capricorn", what_is_my_sign(9, 1))

	def test_8(self):
		self.assertEqual("Scorpio", what_is_my_sign(10, 11))


if __name__ == '__main__':
	unittest.main()