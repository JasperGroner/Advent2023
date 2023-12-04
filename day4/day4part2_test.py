import unittest
from day4part2 import main

class Day4Part2Test(unittest.TestCase):
    def test_sample(self):
        result = main(['testinput.txt'])
        self.assertEqual(result, 30)
    def test_sample_2(self):
        result = main(['realinput.txt'])
        self.assertEqual(result, 5659035)

if __name__ == "__main__":
    unittest.main()
