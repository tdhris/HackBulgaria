import unittest
from zoo_class import Zoo
from animals import Animal


class ZooTests(unittest.TestCase):
    def test_a_zoo_is_created(self):
        my_zoo = Zoo(0, 0)
        self.assertEqual(0, my_zoo.capacity)
        self.assertEqual(0, my_zoo.budget)
        self.assertEqual(0, my_zoo.animal_count)

    def test_representation_is_a_string(self):
        my_zoo = Zoo(100, 600)
        self.assertEqual("Zoo: (100, 600)", str(my_zoo))

    def test_refuses_to_accommodate_if_no_money(self):
        my_zoo = Zoo(100, 0)
        my_animal = Animal("lion", "Terry", 5, 70)
        self.assertFalse(my_zoo.accomodate_animal(1, my_animal))

    def test_accommodates_if_money(self):
        my_zoo = Zoo(100, 500)
        my_animal = Animal("lion", "Terry", 5, 70)
        self.assertTrue(my_zoo.accomodate_animal(1, my_animal))
        self.assertEqual(1, my_zoo.animal_count)

        lion = Animal("lion", "Scar", 15, 70)
        my_zoo.accomodate_animal(2, lion)
        self.assertEqual(2, my_zoo.animal_count)

    def test_gains_calculation(self):
        my_zoo = Zoo(100, 500)
        my_animal = Animal("lion", "Terry", 5, 70)
        my_other_animal = Animal("lion", "Scar", 15, 70)
        my_zoo.accomodate_animal(1, my_animal)
        my_zoo.accomodate_animal(2, my_other_animal)
        self.assertEqual(112, my_zoo.calculate_gains())


if __name__ == '__main__':
    unittest.main()
