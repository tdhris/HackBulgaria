from solution import final_position
import unittest


class OneDimensionalRobotTests(unittest.TestCase):

    def test_final_position_problem_statement_cases(self):
        self.assertEqual(2, final_position("RRLRRLLR", 10, 10))
        self.assertEqual(4, final_position("RRRRR", 3, 4))
        self.assertEqual(-1, final_position("LLLLLLLLLLR", 2, 6))
        self.assertEqual(20, final_position(
            "RRRRRRRLRRLRRRRRRRRRRRRLRLRRRRRRRRLRRRRRLRRRRRRRRR", 5, 20))
        self.assertEqual(-30, final_position("RLRLLLLLLLRLLLRLLLLLLLLRLLLLLRLLLRRLLLLLRLLLLLRLLL", 34, 15))

if __name__ == '__main__':
    unittest.main()