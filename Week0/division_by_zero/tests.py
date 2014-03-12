from division_by_zero import count_numbers
import unittest


class CountNumbersTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_numbers([9, 2]), 3)
        self.assertEqual(count_numbers([8, 2]), 3)
        self.assertEqual(count_numbers([50]), 1)
        self.assertEqual(count_numbers([1, 5, 8, 30, 15, 4]), 11)
        self.assertEqual(count_numbers([1, 2, 4, 8, 16, 32, 64]), 7)
        self.assertEqual(count_numbers([6, 2, 18]), 7)

if __name__ == '__main__':
    unittest.main()
