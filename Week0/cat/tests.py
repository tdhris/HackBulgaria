import sys
import os
import unittest
from solution import cat
from subprocess import check_output

class CatFilesTest(unittest.TestCase):
	def setUp(self):
		self.f = open("blah.txt", "w")

	def test_1(self):
		text = "It's not always easy to distinguish between existentialism and a bad mood."
		self.f.write(text)
		self.f.close()
		content = check_output("python3 solution.py blah.txt", shell = True).decode("utf-8").rstrip("\n")
		self.assertEqual(text, content)

	def test_2(self):
		text = "Build a man a fire, and he'll be warm for a day. Set a man on fire, and he'll be warm for the rest of his life."
		self.f.write(text)
		self.f.close()
		content = check_output("python3 solution.py blah.txt", shell = True).decode("utf-8").rstrip("\n")
		self.assertEqual(text, content)

	def test_3(self):
		text = "A reader lives a thousand lives before he dies, the man who never reads lives only one."
		self.f.write(text)
		self.f.close()
		content = check_output("python3 solution.py blah.txt", shell = True).decode("utf-8").rstrip("\n")
		self.assertEqual(text, content)

	def tearDown(self):
		os.remove("blah.txt")



if __name__ == '__main__':
	os.chdir(os.getcwd() + '/cat')
	unittest.main()
	os.chdir(os.getcwd() + '/..')