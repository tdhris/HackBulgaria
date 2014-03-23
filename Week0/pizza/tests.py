import unittest
import solution
import os


class PizzaTests(unittest.TestCase):
    def setUp(self):
        self.a = open("archive.txt", "w")

    def test_take(self):
        command = "take Tyrion 3.45"
        self.assertEqual(['take', 'Tyrion', '3.45'], solution.take(command))

    def test_save_load(self):
        orders = {'Tyrion': '3.45', 'Kvothe': '4.62'}
        number_saves = 1
        solution.save(orders, number_saves)
        self.assertEqual({'Tyrion': '3.45', 'Kvothe': '4.62'}, solution.load("load 1"))

    def test_status(self):
        self.assertEqual(True, solution.print_status({'Tyrion': '3.45', 'Kvothe': '4.62'}))

    def test_print_list(self):
        self.assertEqual(True, solution.print_list())

    def tearDown(self):
        for file in os.listdir(os.getcwd()):
            if file.endswith(".txt") and file != "menu_commands.txt" and file != "unsaved_order.txt":
                os.remove(file)


if __name__ == '__main__':
    unittest.main()
