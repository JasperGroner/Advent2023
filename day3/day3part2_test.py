import unittest
from day3part2 import main

class Day3Part2Test(unittest.TestCase):
    def test_sample(self):
        result = main(['testinput.txt'])
        self.assertEqual(result, 467835)
    def test_sample_2(self):
        result = main(['realinput.txt'])
        self.assertEqual(result, 84584891)

if __name__ == "__main__":
    unittest.main()
