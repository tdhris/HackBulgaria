import unittest
import os
from solution import ext

class ExtTest(unittest.TestCase):
	def setUp(self):
		self.f = open("muh.gif", "w").close()
		self.f = open("huh.gif", "w").close()
		self.f = open("duh.gif", "w").close()
		self.f = open("vuh.txt", "w").close()
		self.f = open("puh.jpg", "w").close()
		self.path = os.getcwd()

	def test_gif(self):
		self.assertEqual(3, ext(self.path, ".gif"))

	def test_txt(self):
		self.assertEqual(1, ext(self.path, ".txt"))
		self.assertEqual(0, ext(self.path, "txt"))
		
	def test_jpg(self):
		self.assertEqual(1, ext(self.path, ".jpg"))

def tearDown(self):
		os.remove("vuh.txt")
		os.remove("muh.gif")
		os.remove("huh.gif")
		os.remove("duh.gif")
		os.remove("puh.jpg")


if __name__ == '__main__':
	unittest.main()