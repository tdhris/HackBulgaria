from anaconda import Anaconda
import unittest


class AnacondaTests(unittest.TestCase):
    def setUp(self):
        self.snake = Anaconda(100)

    def test_creation(self):
        self.assertTrue(self.snake.attacks_necessary <= 10)
        self.assertTrue(self.snake.attacks_necessary >= 3)
        self.assertTrue(self.snake.berserk_factor <= 2.0)
        self.assertTrue(self.snake.berserk_factor >= 1.0)
        self.assertEqual(0, self.snake.attack_count)

    def test_representation(self):
        self.assertTrue('the ANACONDA' in str(self.snake))

    def test_attack(self):
        self.assertTrue(self.snake.attack())

    def test_berserk_attack(self):
        self.snake.attacks_necessary = 2
        self.snake.berserk_factor = 2.0
        self.snake.damage = 20
        self.assertEqual(20, self.snake.attack())
        self.assertEqual(40, self.snake.attack())

if __name__ == '__main__':
    unittest.main()
