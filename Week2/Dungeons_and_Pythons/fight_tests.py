import unittest
import entity
import fight
import weapon

class FightTests(unittest.TestCase):

	def setUp(self):
		self.hero = entity.Hero("Jack Sparrow", 100, "the Captain")
		self.orc = entity.Orc("Davy Jones", 100, 1.2)
		self.f = fight.Fight(self.hero, self.orc)

		weapon_1 = weapon.Weapon("axe", 24, 0.2)
		weapon_2 = weapon.Weapon("sword", 32, 0.3)
		self.hero.equip_weapon(weapon_1)
		self.orc.equip_weapon(weapon_2)

	# def test_flip_coin_for_first(self):
	# 	self.assertEqual(self.hero, self.f.who_is_first())

	def test_simulate_fight(self):
		self.assertEqual(True, self.f.simulate_fight())

if __name__ == '__main__':
	unittest.main()
