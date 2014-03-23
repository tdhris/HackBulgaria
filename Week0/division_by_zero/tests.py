from solution import count_numbers
import unittest


class CountNumbersTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_numbers([9, 2]), 3)

    def test_2(self):
        self.assertEqual(count_numbers([8, 2]), 3)

    def test_3(self):
        self.assertEqual(count_numbers([50]), 1)

    def test_4(self):
        self.assertEqual(count_numbers([1, 5, 8, 30, 15, 4]), 10)

    def test_5(self):
        self.assertEqual(count_numbers([1, 2, 4, 8, 16, 32, 64]), 7)

    def test_6(self):
        self.assertEqual(count_numbers([6, 2, 18]), 7)

if __name__ == '__main__':
    unittest.main()
