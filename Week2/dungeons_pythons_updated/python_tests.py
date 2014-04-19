from python import Python
import unittest


class PythonTests(unittest.TestCase):
    def setUp(self):
        self.snake = Python(100)

    def test_creation(self):
        self.assertTrue(self.snake.damage >= 2)
        self.assertTrue(self.snake.damage <= 30)

    def test_representation(self):
        self.assertTrue('the Python' in str(self.snake))

    def test_attack(self):
        self.assertTrue(self.snake.attack())


if __name__ == '__main__':
    unittest.main()
