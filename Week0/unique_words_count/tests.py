import unittest
from solution import unique_words_count

class UniqueWordsTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual(3, unique_words_count(["apple", "banana", "apple", "pie"]))

	def test_2(self):
		self.assertEqual(2, unique_words_count(["python", "python", "python", "ruby"]))

	def test_3(self):
		self.assertEqual(1, unique_words_count(["HELLO!"] * 10))


if __name__ == '__main__':
	unittest.main()