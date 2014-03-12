import unittest
from solution import is_prime

class PrimeTests(unittest.TestCase):

	 def test_prime(self):
	 	self.assertTrue(is_prime(2))
	 	self.assertTrue(is_prime(11))
	 	self.assertTrue(is_prime(601))
	 	self.assertTrue(is_prime(419))

	 def test_not_prime(self):
	 	self.assertFalse(is_prime(1))
	 	self.assertFalse(is_prime(8))
	 	self.assertFalse(is_prime(-10))
	 	self.assertFalse(is_prime(420))


if __name__ == '__main__':
	unittest.main()