import unittest
from day5part1 import main

class Day5Part1Test(unittest.TestCase):
    def test_sample(self):
        result = main(['testinput.txt'])
        self.assertEqual(result, 35)
    def test_sample_2(self):
        result = main(['realinput.txt'])
        self.assertEqual(result, 484023871)

if __name__ == "__main__":
    unittest.main()
