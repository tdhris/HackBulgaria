from solution import member_of_nth_fib_lists
import unittest

class MemberNthFib(unittest.TestCase):

	def test_1(self):
		self.assertEqual(False, member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
		self.assertEqual(True, member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))
		self.assertEqual(True, member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))
		self.assertEqual(False, member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))



if __name__ == '__main__':
	unittest.main()