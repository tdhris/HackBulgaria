import unittest
from subprocess import call
from solution import ext

class ExtTest(unittest.TestCase):
	def test_gif(self):
		self.assertEqual(3, ext(".gif"))
	def test_cpp(self):
		self.assertEqual(2, ext(".cpp"))
	def test_py(self):
		self.assertEqual(2, ext(".py"))
	def test_non_ext(self):
		self.assertEqual(0, ext("py"))

if __name__ == '__main__':
	unittest.main()
