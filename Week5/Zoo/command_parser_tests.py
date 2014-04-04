import unittest
from command_parser import CommandParser


class CommandParserTests(unittest.TestCase):
    def test_add_function(self):
        self.parser = CommandParser()

        def get_baba():
            return "baba"

        self.parser.add_function("baba", get_baba)

        self.assertIn("baba", self.parser.functions)

    def test_take_command(self):
        self.parser = CommandParser()

        def get_baba(arguments):
            return "baba"

        self.parser.add_function("baba", get_baba)
        self.assertEqual("baba", self.parser.take_command("baba"))

if __name__ == '__main__':
    unittest.main()
