import unittest
from entity import Entity


class EntityTests(unittest.TestCase):
    def setUp(self):
        self.h = Entity(100)

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

if __name__ == '__main__':
    unittest.main()
