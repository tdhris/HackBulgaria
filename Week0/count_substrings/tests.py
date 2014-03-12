from solution import count_substrings
import unittest

class CountSubstringsTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual(2, count_substrings("This is a test string", "is"))
	def test_2(self):
		self.assertEqual(2, count_substrings("babababa", "baba"))
	def test_3(self):
		self.assertEqual(4, count_substrings("Python is an awesome language to program in!", "o"))
	def test_4(self):
		self.assertEqual(0, count_substrings("We have nothing in common!", "really?"))
	def test_5(self):
		self.assertEqual(2, count_substrings("This is this and that is this", "this"))




if __name__ == '__main__':
	unittest.main()