import unittest
from animals import Animal


class AnimalTests(unittest.TestCase):
    def setUp(self):
        self.animal = Animal('lion', 'Nala', 3, 130)
        self.animal.gender = 'f'

    def test_sepcie(self):
        self.assertEqual('lion', self.animal.specie)

    def test_age(self):
        self.assertEqual(3, self.animal.age)

    def test_name_and_weight(self):
        self.assertEqual('Nala', self.animal.name)
        self.assertEqual(130, self.animal.weight)

    def test_chance_of_dying(self):
        self.assertEqual(10, self.animal.chance_of_dying)

    def test_default_values(self):
        self.assertEqual(1, self.animal.dead_or_alive)
        self.assertEqual(0, self.animal.time_since_last_birth)
        self.assertEqual(0, self.animal.is_pregnant)

    def test_representation(self):
        self.assertEqual('Nala - species: lion, age: 3, weight: 130, gender: female', str(self.animal))

    def test_expense(self):
        expense = 9
        self.assertEqual(expense, self.animal.expense)

    def test_can_breed(self):
        self.assertTrue(self.animal.can_breed())

    def test_get_gestation(self):
        self.assertEqual(3, self.animal.get_gestation())

if __name__ == '__main__':
    unittest.main()
