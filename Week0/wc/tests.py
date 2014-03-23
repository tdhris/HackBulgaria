import unittest
import os
from subprocess import check_output
from solution import count_chars
from solution import count_words
from solution import count_lines

class CountTests(unittest.TestCase):
	def test_chars(self):
		self.assertEqual(1032, count_chars("story.txt"))
		output = check_output("python3 solution.py chars story.txt", shell=True).decode("utf-8").rstrip('\n')
		self.assertEqual(int(output), 1032)

	def test_lines(self):
		self.assertEqual(6, count_lines("story.txt"))
		output = check_output("python3 solution.py lines story.txt", shell=True).decode("utf-8").rstrip('\n')
		self.assertEqual(int(output), 6)

	def test_words(self):
		self.assertEqual(166, count_words("story.txt"))
		output = check_output("python3 solution.py words story.txt", shell=True).decode("utf-8").rstrip('\n')
		self.assertEqual(int(output), 166)


if __name__ == '__main__':
    os.chdir(os.getcwd() + '/wc')
    unittest.main()
    os.chdir(os.getcwd() + '/..')