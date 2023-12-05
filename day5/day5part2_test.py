import unittest
from day5part2 import main

class Day5Part2Test(unittest.TestCase):
    def test_sample(self):
        result = main(['testinput.txt'])
        self.assertEqual(result, 46)
    def test_sample_2(self):
        result = main(['realinput.txt'])
        self.assertEqual(result, 46294175)
        
if __name__ == "__main__":
    unittest.main()
