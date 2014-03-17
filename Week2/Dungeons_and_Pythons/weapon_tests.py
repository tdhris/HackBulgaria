import unittest
import entity
import weapon

class WeaponTests(unittest.TestCase):

	def setUp(self):
		self.w = weapon.Weapon("sword", 50, 1.0)

	def test_type(self):
		self.assertEqual("sword", self.w.get_weapon())

	def test_critical_damage_100(self):
		self.assertEqual(True, self.w.critical_hit())

	def test_crit_hit_chance_0(self):
		self.w.critical_strike_percent = 0.0
		self.assertEqual(False, self.w.critical_hit())

	def test_random(self):
		self.w.critical_strike_percent = 0.7
		print(self.w.critical_hit())


if __name__ == '__main__':
	unittest.main()