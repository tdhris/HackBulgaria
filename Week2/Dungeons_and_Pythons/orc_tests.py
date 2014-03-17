import unittest
import orc

class OrcTests(unittest.TestCase):

	def setUp(self):
		self.o = orc.Orc("Gurgh", 100, 1.5)

	def test_get_health(self):
		self.assertEqual(100, self.o.get_health())

	def test_take_damage(self):
		self.assertEqual(True, self.o.take_damage(50))
		self.assertEqual(50, self.o.get_health())

	def test_take_more_damage_than_health_points(self):
		self.assertEqual(self.o.take_damage(200), False)
		self.assertEqual(0, self.o.get_health())

	def test_is_alive(self):
		self.o.take_damage(100)
		self.assertEqual(False, self.o.is_alive())

	def test_take_healing(self):
		self.o.take_damage(50)
		self.assertEqual(True, self.o.take_healing(30))
		self.assertEqual(80, self.o.get_health())

	def test_take_more_healing_than_needed(self):
		self.o.take_damage(50)
		self.assertEqual(50, self.o.get_health())
		self.assertEqual(False, self.o.take_healing(70))
		self.assertEqual(100, self.o.get_health())

if __name__ == '__main__':
	unittest.main()
