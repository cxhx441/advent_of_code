import unittest
from d10 import *

class Solution1Test(unittest.TestCase):
    def test_input_parsing_on_example(self):
        grid = parse_input("puzzle_input/d10_input_ex1.txt")
        seeking = [
            [0,1,2,3],
            [1,2,3,4],
            [8,7,6,5],
            [9,8,7,6]
        ]
        self.assertEqual(grid, seeking)

    def test_solution1_result_on_example1(self):
        grid = parse_input("puzzle_input//d10_input_ex1.txt")
        result = solution_1(grid)
        self.assertEqual(result, 1)  # add assertion here

    def test_solution1_result_on_example2(self):
        grid = parse_input("puzzle_input//d10_input_ex2.txt")
        result = solution_1(grid)
        self.assertEqual(result, 36)  # add assertion here


class Solution2Test(unittest.TestCase):
    def test_solution2_result_on_example(self):
        grid = parse_input("puzzle_input//d10_input_ex2.txt")
        result = solution_2(grid)
        self.assertEqual(result, 81)  # add assertion here

if __name__ == '__main__':
    unittest.main()
