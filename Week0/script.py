from glob import glob
import os
from subprocess import call


def run_all_tests():
    tests = glob('*/tests.py')
    for test in tests:
        call("python3 " + test, shell=True)
    return True


def main():
    run_all_tests()
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            os.remove(file)

if __name__ == '__main__':
    main()
