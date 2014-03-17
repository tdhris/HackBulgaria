import unittest
import solution

class BankClass(unittest.TestCase):

	def test_get_balance_zero(self):
		solution.balance = 0
		self.assertEqual(0, solution.get_balance())

	def test_get_balance_nonzero(self):
		solution.balance = 100
		self.assertEqual(100, solution.get_balance())
		solution.balance = 300
		self.assertEqual(300, solution.get_balance())
	
	def test_deposit(self):
		solution.balance = 0
		self.assertTrue(solution.deposit_money(100))
		solution.deposit_money(100)
		self.assertEqual(200, solution.get_balance())

	def test_withdraw(self):
		solution.balance = 40
		self.assertTrue(solution.withdraw_money(30))

	def test_withdraw_more_than_balance(self):
		solution.balance = 0
		self.assertEqual(0, solution.get_balance())
		self.assertFalse(solution.withdraw_money(100))

		

if __name__ == '__main__':
	unittest.main()
