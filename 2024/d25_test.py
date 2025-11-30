import unittest

from d25 import *

class Solution1Test(unittest.TestCase):
    def test_solution1_on_ex1(self):
        unlocked = solution_1("puzzle_input/d25_input_ex1.txt")
        self.assertEqual(unlocked, 3)

if __name__ == '__main__':
    unittest.main()
