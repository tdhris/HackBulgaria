import unittest
from hero import Hero
from weapon import Weapon


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.h = Hero("Blah", 100, "the Blah")

    def test_hero_name(self):
        self.assertEqual(self.h.name, "Blah")

    def test_known_as(self):
        self.assertEqual("Blah the Blah", self.h.known_as())

    def test_get_health(self):
        self.assertEqual(100, self.h.get_health())

    def test_is_alive_full_health(self):
        self.assertEqual(True, self.h.is_alive())

    def test_take_healing(self):
        self.h.take_damage(50)
        self.assertEqual(True, self.h.take_healing(30))
        self.assertEqual(80, self.h.get_health())

    def test_take_more_healing_than_needed(self):
        self.h.take_damage(50)
        self.assertEqual(50, self.h.get_health())
        self.assertEqual(False, self.h.take_healing(70))
        self.assertEqual(100, self.h.get_health())

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

    def test_equip_weapon(self):
        w = Weapon("sword", 50, 0.7)
        self.assertEqual(True, self.h.equip_weapon(w))
        self.assertEqual(w, self.h.weapon)

    def test_attack(self):
        self.assertEqual(10, self.h.attack())
        w = Weapon("sword", 50, 0)
        self.assertEqual(True, self.h.equip_weapon(w))
        self.assertEqual(50, self.h.attack())

    def test_fail_equipment(self):
        self.assertEqual(False, self.h.equip_weapon("not a weapon"))

    def test_equipment(self):
        w = Weapon("grandma's cake", 99, 0.5)
        self.h.equip_weapon(w)
        self.assertEqual(w.type, self.h.weapon.type)
        w_second = Weapon("grandpa's tong", 100, 1.0)
        self.h.equip_weapon(w_second)
        self.assertEqual(w_second.type, self.h.weapon.type)


if __name__ == '__main__':
    unittest.main()
