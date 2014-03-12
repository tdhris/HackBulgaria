from solution import count_consonants
import unittest

class CountConsonantsTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual(4, count_consonants("Python"))

	def test_2(self):
		self.assertEqual(11, count_consonants("Theistareykjarbunga"))

	def test_3(self):
		self.assertEqual(7, count_consonants("grrrrgh!"))

	def test_4(self):
		self.assertEqual(44, count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

	def test_5(self):
		self.assertEqual(6, count_consonants("A nice day to code!"))




if __name__ == '__main__':
	unittest.main()