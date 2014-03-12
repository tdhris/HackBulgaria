import unittest
from solution import reduce_file_path

class ReducePathTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual("/", reduce_file_path("/"))

	def test_2(self):
		self.assertEqual("/", reduce_file_path("/srv/../"))

	def test_3(self):
		self.assertEqual("/srv/www/htdocs/wtf", reduce_file_path("/srv/www/htdocs/wtf/"))

	def test_4(self):
		self.assertEqual("/srv/www/htdocs/wtf", reduce_file_path("/srv/www/htdocs/wtf"))

	def test_5(self):
		self.assertEqual("/srv", reduce_file_path("/srv/./././././"))

	def test_6(self):
		self.assertEqual("/etc/wtf", reduce_file_path("/etc//wtf/"))

	def test_7(self):
		self.assertEqual("/", reduce_file_path("/etc/../etc/../etc/../"))

	def test_8(self):
		self.assertEqual("/", reduce_file_path("//////////////"))

	def test_9(self):
		self.assertEqual("/", reduce_file_path("/../"))



if __name__ == '__main__':
	unittest.main()