import unittest
import os
from subprocess import call
from solution import concat_files

class ConcatFilesTests(unittest.TestCase):
	def setUp(self):
		self.mega = open("MEGATRON.txt", "w")
		self.mega.close()
		self.f = open("file_1.txt", "w")
		self.f.write("There's real poetry in the real world.")
		self.f.close()
		self.f = open("file_2.txt", "w")
		self.f.write("Science is the poetry of reality.")
		self.f.close()

	def test_1(self):
		text = "There's real poetry in the real world.Science is the poetry of reality."
		concat_files(["file_1.txt", "file_2.txt"])
		file = open("MEGATRON.txt", "r")
		content = file.read().rstrip('\n')
		file.close()
		self.assertEqual(content, text)

	def tearDown(self):
		for file in os.listdir(os.getcwd()):
			if file.endswith(".txt"):
				os.remove(file)


if __name__ == '__main__':
	if not os.getcwd().endswith('/concat_files'):
		os.chdir(os.getcwd() + '/concat_files')
	unittest.main()
	os.chdir(os.getcwd() + '/..')
