import unittest
import entity
import weapon

class EntityTests(unittest.TestCase):

	def setUp(self):
		self.h = entity.Hero("Blah", 100, "the Brave")
		self.o = entity.Orc("Grhuuugh", 100, 1.3)

	def test_get_health(self):
		self.assertEqual(100, self.h.get_health())

	def test_take_damage(self):
		self.assertEqual(True, self.h.take_damage(50))
		self.assertEqual(50, self.h.get_health())

	def test_take_more_damage_than_health_points(self):
		self.assertEqual(self.h.take_damage(200), False)
		self.assertEqual(0, self.h.get_health())

	def test_is_alive(self):
		self.h.take_damage(100)
		self.assertEqual(False, self.h.is_alive())

	def test_take_healing(self):
		self.h.take_damage(50)
		self.assertEqual(True, self.h.take_healing(30))
		self.assertEqual(80, self.h.get_health())

	def test_take_more_healing_than_needed(self):
		self.h.take_damage(50)
		self.assertEqual(50, self.h.get_health())
		self.assertEqual(False, self.h.take_healing(70))
		self.assertEqual(100, self.h.get_health())

	def test_has_weapon(self):
		self.assertEqual(False, self.h.has_weapon())

	def test_equip_weapon(self):
		w = weapon.Weapon("sword", 50, 0.7)
		self.assertEqual(True, self.h.equip_weapon(w))
		self.assertEqual(True, self.h.has_weapon())

	def test_attack(self):
		self.assertEqual(0, self.h.attack())
		w = weapon.Weapon("sword", 50, 0.7)
		self.assertEqual(True, self.h.equip_weapon(w))
		self.assertEqual(50, self.h.attack())

	def test_fail_equipment(self):
		self.assertEqual(False, self.h.equip_weapon("not a weapon"))

	def test_equipment(self):
		w = weapon.Weapon("grandma's cake", 99, 0.5)
		self.h.equip_weapon(w)
		self.assertEqual(True, self.h.has_weapon())
		w_second = weapon.Weapon("grandpa's tong", 100, 1.0)
		self.h.equip_weapon(w_second)
		self.assertEqual(w_second.type, self.h.weapon.type)

	def test_berserks(self):
		w = weapon.Weapon("grandma's cake", 99, 0.5)
		self.o.equip_weapon(w)
		self.assertEqual(True, self.o.has_weapon())
		self.assertEqual(self.o.weapon.damage * self.o.berserk_factor, self.o.attack())

		

if __name__ == '__main__':
	unittest.main()