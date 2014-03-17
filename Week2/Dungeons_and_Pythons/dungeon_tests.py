import unittest
import entity
import dungeon
import weapon

class DungeonsTests(unittest.TestCase):

	def setUp(self):
		self.h = entity.Hero("Blah", 100, "the Brave")
		self.o = entity.Orc("Grhuuugh", 100, 1.3)
		self.m = dungeon.Dungeon("map.txt")
		self.assertEqual(True, self.m.spawn("hero", self.h))
		self.assertEqual(True, self.m.spawn("orc", self.o))

		weapon_1 = weapon.Weapon("axe", 24, 0.2)
		weapon_2 = weapon.Weapon("sword", 32, 0.3)
		self.h.equip_weapon(weapon_1)
		self.o.equip_weapon(weapon_2)


	def test_fail_spawn(self):
		self.assertEqual(False, self.m.spawn("orc", 473))

	def test_make_move(self):
		self.assertEqual(False, self.m.move("hero", 'up'))
		self.assertEqual(False, self.m.move("hero", "down"))
		self.assertEqual(False, self.m.move("hero", "left"))
		self.assertEqual(True, self.m.move("hero", "right"))
		self.assertEqual(True, self.m.move("hero", "down"))

	def test_fight(self):
		self.assertEqual(True, self.m.move("hero", "right"))
		self.assertEqual(True, self.m.move("hero", "down"))
		self.assertEqual(True, self.m.move("hero", "down"))
		self.assertEqual(True, self.m.move("hero", "down"))
		self.assertEqual(True, self.m.move("hero", "right"))
		self.assertEqual(True, self.m.move("hero", "right"))
		self.assertEqual(True, self.m.move("hero", "right"))
		self.assertEqual(True, self.m.move("hero", "right"))
		self.assertEqual(True, self.m.move("hero", "up"))
		self.assertEqual(True, self.m.move("hero", "up"))
		self.assertEqual(True, self.m.move("hero", "up"))
		self.assertEqual(True, self.m.move("hero", "right"))
		self.assertEqual(True, self.m.move("hero", "right"))
		self.assertEqual(True, self.m.move("hero", "right"))
		self.assertEqual(True, self.m.move("hero", "right"))
		self.assertEqual(True, self.m.move("hero", "down"))
		self.assertEqual(True, self.m.move("hero", "down"))
		self.assertEqual(True, self.m.move("orc", "up"))
		self.m.move("orc", "up")




if __name__ == '__main__':
	unittest.main()