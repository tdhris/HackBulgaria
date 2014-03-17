import unittest
from solution import sum_numbers

class SumNumbersTests(unittest.TestCase):
	def setUp(self):
		self.f = open("numbers.txt", "w")
		self.f.write("1 2 3 4 5 6 7 8")
		self.f.close()

	def test_1(self):
		self.assertEqual(36, sum_numbers("numbers.txt"))

	def test_2(self):
		self.f = open("numbers.txt", "a")
		self.f.write(" 9 10 11")
		self.f.close()
		self.assertEqual(66, sum_numbers("numbers.txt"))

	def test_3(self):
		self.assertRaises(sum_numbers("nonexisting_file.txt"))


if __name__ == '__main__':
	unittest.main()