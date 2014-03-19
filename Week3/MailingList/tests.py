import unittest
import os
import mail
import printing_functions
import List

class MailTests(unittest.TestCase):
	def setUp(self):
		List.create_archive()
		self.l = List.List('Hack BG')

	def test_constructor_creates_file_for_list(self):
		does_list_file_exist = False

		working_directory = os.getcwd()
		for file in os.listdir(working_directory):
			if file == 'Hack_BG.txt':
				does_list_file_exist = True
				break

		self.assertTrue(does_list_file_exist)
		
	def test_constuctor_add_list_to_archive(self):
		self.f = open("archive.txt", "r")
		content = self.f.read().rstrip('\n')
		self.f.close()
		self.assertEqual("[1] Hack BG", content)

	def test_get_arguments(self):
		c = "merge 1 2 HACK_LIST"
		a = List.get_arguments(c, 3)
		self.assertEqual(['1', '2', 'HACK_LIST'], a)

	def test_get_valid_filename(self):
		list_name = "Hack BG Not Valid Filename"
		self.assertEqual("Hack_BG_Not_Valid_Filename.txt", List.get_valid_filename(list_name))
		list_name = "HackBG"
		self.assertEqual("HackBG.txt", List.get_valid_filename(list_name))
		line_of_file = "[1] John Smith - jsmith@gmail.com"


if __name__ == '__main__':
	unittest.main()
