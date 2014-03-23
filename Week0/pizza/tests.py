import unittest
import solution


class PizzaTests(unittest.TestCase):
    def test_take(self):
        command = "take Tanya 3.45"
        self.assertEqual(['take', 'Tanya', '3.45'], solution.take(command))

    def test_save_load(self):
        orders = {'Tanya': '3.45', 'Plami': '4.62'}
        number_saves = 1
        solution.save(orders, number_saves)
        self.assertEqual({'Tanya': '3.45', 'Plami': '4.62'}, solution.load("load 1"))

    def test_status(self):
        self.assertEqual(True, solution.print_status({'Tanya': '3.45', 'Plami': '4.62'}))

    def test_print_list(self):
        self.assertEqual(True, solution.print_list())


if __name__ == '__main__':
    unittest.main()
