import unittest
import hero

class HeroTests(unittest.TestCase):

	def setUp(self):
		self.h = hero.Hero("Blah", "the Blah", 100)

	def test_hero_name(self):
		self.assertEqual(self.h.name, "Blah")

	def test_known_as(self):
		self.assertEqual("Blah the Blah", self.h.known_as())

	def test_get_health(self):
		self.assertEqual(100, self.h.get_health())

	def test_is_alive_full_health(self):
		self.assertEqual(True, self.h.is_alive())

	def test_damage_hero(self):
		self.assertEqual(True, self.h.take_damage(50))
		self.assertEqual(50, self.h.get_health())

	def test_damage_hero_with_more_points_than_he_has_in_health(self):
		self.assertEqual(False, self.h.take_damage(200))
		self.assertEqual(0, self.h.get_health())
		self.assertEqual(False, self.h.is_alive())

	def test_healing(self):
		self.h.take_damage(50)
		self.assertEqual(50, self.h.get_health())
		self.assertEqual(True, self.h.take_healing(50))
		self.assertEqual(100, self.h.get_health())

	def test_healing_with_more_points_than_are_needed(self):
		self.h.take_damage(50)
		self.assertEqual(50, self.h.get_health())
		self.assertEqual(False, self.h.take_healing(150))
		self.assertEqual(100, self.h.get_health())

	def test_heal_dead_hero(self):
		self.h.take_damage(100)
		self.assertEqual(False, self.h.is_alive())
		self.assertEqual(False, self.h.take_healing(30))
		self.assertEqual(0, self.h.get_health())

if __name__ == '__main__':
	unittest.main()