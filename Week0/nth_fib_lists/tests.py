import unittest
from solution import nth_fib_lists

class NFibListTest(unittest.TestCase):

	def test_1(self):
		self.assertEqual([1], nth_fib_lists([1], [2], 1))
		self.assertEqual([2], nth_fib_lists([1], [2], 2))

	def test_2(self):
		self.assertEqual([1, 2, 1, 3], nth_fib_lists([1, 2], [1, 3], 3))

	def test_3(self):
		self.assertEqual([1, 2, 3, 1, 2, 3], nth_fib_lists([], [1, 2, 3], 4))

	def test_4(self):
		self.assertEqual([], nth_fib_lists([], [], 100))

if __name__ == '__main__':
	unittest.main()