import unittest
from string_utils import lines
from string_utils import unlines
from string_utils import words
from string_utils import unwords
from string_utils import tabs_to_spaces

class StringUtilsTests(unittest.TestCase):
	def test_lines(self):
		self.assertEqual(['new', 'line'], lines("new\nline"))
		self.assertEqual(['Everything starts somewhere,', 'although many physicists disagree.'], lines("Everything starts somewhere,\nalthough many physicists disagree."))

	def test_unlines(self):
		self.assertEqual("All\nchildren\nexcept\none\ngrow\nup", unlines(["All", "children", "except", "one", "grow", "up"]))

	def test_words(self):
		self.assertEqual(["a", "good", "confidence", "game", "took", "three", "months", "to", "plan,", "three", "weeks", "to", "rehearse,", "and", "three", "seconds", "to", "win", "or", "lose", "the", "victim's", "trust", "forever."],
			words("a good confidence game took three months to plan, three weeks to rehearse, and three seconds to win or lose the victim's trust forever."))

	def test_unwords(self):
		self.assertEqual("The circus arrives without warning", unwords(["The", "circus", "arrives", "without", "warning"]))

	def test_tabs_to_spaces(self):
		self.assertEqual("a     b", tabs_to_spaces("a\tb", 5))
		self.assertEqual("a b", tabs_to_spaces("a\tb", 1))

if __name__ == '__main__':
	unittest.main()