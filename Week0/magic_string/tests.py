from solution import magic_string
import unittest


class MagicStringTest(unittest.TestCase):
    def test_problem_statement_cases(self):
        self.assertEqual(2, magic_string(">><<><"))
        self.assertEqual(0, magic_string(">>>><<<<"))
        self.assertEqual(4, magic_string("<<>>"))
        self.assertEqual(20,
                         magic_string(
                         "<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"))

if __name__ == '__main__':
    unittest.main()
