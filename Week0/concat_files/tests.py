import unittest
from subprocess import check_output
from solution import concat_files

class ConcatFilesTests(unittest.TestCase):
	def setUp(self):
		self.f = open("file_1.txt", "w")
		self.f.write("There's real poetry in the real world.")
		self.f.close()
		self.f = open("file_2.txt", "w")
		self.f.write("Science is the poetry of reality.")
		self.f.close()

	def test_1(self):
		files = ["file_1.txt", "file_2.txt"]
		concat_files(files)
		self.f = open("MEGATRON.txt", "r")
		content = self.f.read().rstrip('\n')
		self.f.close()
		output = check_output("cat MEGATRON.txt", shell=True).decode("utf-8").rstrip('\n')
		self.assertEqual(content, output)

if __name__ == '__main__':
	unittest.main()
