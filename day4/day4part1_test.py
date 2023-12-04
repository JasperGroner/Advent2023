import unittest
from day4part1 import main

class Day4Part1Test(unittest.TestCase):
    def test_sample(self):
        result = main(['testinput.txt'])
        self.assertEqual(result, 13)
    def test_sample_2(self):
        result = main(['realinput.txt'])
        self.assertEqual(result, 24160)

if __name__ == "__main__":
    unittest.main()
