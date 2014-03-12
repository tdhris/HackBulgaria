from solution import is_an_bn
import unittest

class AnBnTest(unittest.TestCase):
	def test_1(self):
		self.assertEqual(True, is_an_bn(""))
	def test_2(self):
		self.assertEqual(False, is_an_bn("rado"))
	def test_3(self):
		self.assertEqual(False, is_an_bn("aaabb"))
	def test_4(self):
		self.assertEqual(True, is_an_bn("aaabbb"))
	def test_5(self):
		self.assertEqual(False, is_an_bn("aabbaabb"))
	def test_6(self):
		self.assertEqual(False, is_an_bn("bbbaaa"))
	def test_7(self):
		self.assertEqual(True,is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
	unittest.main()