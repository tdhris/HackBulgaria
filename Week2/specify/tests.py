import unittest
import os
from subprocess import call
from solution import specify

class SpecifyTest(unittest.TestCase):
	def setUp(self):
		self.f = open("random.txt", "w")
		self.f.write("\tha\tha")
		self.f.close()

	def test_specify1(self):
		result = call("python3 solution.py random.txt", shell = True)
		self.f = open("random.txt", "r")
		contents = self.f.read()
		self.f.close()
		self.assertEqual("    ha    ha", contents)

	def tearDown(self):
		os.remove("random.txt")

if __name__ == '__main__':
	unittest.main()

