import unittest
from subprocess import check_output


class CatMultiFilesTest(unittest.TestCase):

    def setUp(self):
        self.f = open("cool.txt", "w")

    def test_one_file(self):
        text = "There's never been a true war that wasn't fought between two sets of people who were certain they were in the right"
        self.f.write(text)
        self.f.close()
        self.f = open("cool.txt", "r")
        content = check_output("python3 solution.py cool.txt", shell = True).decode("utf-8").rstrip("\n")
        self.assertEqual(text, content)

    def test_two_files(self):
        text = ''
        text_first = "Not all those"
        text += text_first + '\n'
        self.f.write(text_first)
        self.f.close()

        text_second = "who wander are lost"
        text += text_second
        self.f = open("huh.txt", "w")
        self.f.write(text_second)
        self.f.close()

        content = check_output("python3 solution.py cool.txt huh.txt", shell = True).decode("utf-8").rstrip("\n")
        self.assertEqual(text, content)



if __name__ == '__main__':
    unittest.main()
