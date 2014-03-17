import unittest
from solution import generate_numbers

class GenerateNumbersTests(unittest.TestCase):

	def test_1(self):
		generate_numbers("numbers.txt", 10)
		self.f = open("numbers.txt", "r")
		content = self.f.read().rstrip('\n')
		self.f.close()
		count = 0
		for num in content.split():
			count+=1
		self.assertEqual(10, count)

	def test_2(self):
		generate_numbers("numbers2.txt", 20)
		self.f = open("numbers2.txt", "r")
		content = self.f.read().rstrip('\n')
		self.f.close()
		count = 0
		for num in content.split():
			count+=1
		self.assertEqual(20, count)

	def test_3(self):
		generate_numbers("numbers3.txt", 50)
		self.f = open("numbers3.txt", "r")
		content = self.f.read().rstrip('\n')
		self.f.close()
		count = 0
		for num in content.split():
			count+=1
		self.assertEqual(50, count)

	def test_4(self):
		self.assertRaises(generate_numbers("numbers_failure.txt", -45))


if __name__ == '__main__':
	unittest.main()


