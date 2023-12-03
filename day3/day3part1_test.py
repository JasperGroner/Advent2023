import unittest
from day3part1 import main

class Day3Part1Test(unittest.TestCase):
    def test_sample(self):
        result = main(['testinput.txt'])
        self.assertEqual(result, 4361)
    def test_sample_2(self):
        result = main(['realinput.txt'])
        self.assertEqual(result, 540025)

if __name__ == "__main__":
    unittest.main()
