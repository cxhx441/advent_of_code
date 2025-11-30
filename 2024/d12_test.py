import unittest
from d12 import *

class Solution1Test(unittest.TestCase):
    def test_input_parsing_on_example(self):
        grid = parse_input("puzzle_input/d12_input_ex1.txt")
        seeking = [
            ['A', 'A', 'A', 'A'],
            ['B', 'B', 'C', 'D'],
            ['B', 'B', 'C', 'C'],
            ['E', 'E', 'E', 'C'],
        ]
        self.assertEqual(grid, seeking)

    def test_solution1_result_on_example1(self):
        grid = parse_input("puzzle_input//d12_input_ex1.txt")
        result = solution_1(grid)
        self.assertEqual(result, 140)  # add assertion here

    def test_solution1_result_on_example2(self):
        grid = parse_input("puzzle_input//d12_input_ex2.txt")
        result = solution_1(grid)
        self.assertEqual(result, 772)  # add assertion here

class Solution2Test(unittest.TestCase):
    def test_solution2_result_on_example1(self):
        grid = parse_input("puzzle_input//d12_input_ex1.txt")
        result = solution_2(grid)
        self.assertEqual(result, 80)  # add assertion here

    def test_solution2_result_on_example2(self):
        grid = parse_input("puzzle_input//d12_input_ex2.txt")
        result = solution_2(grid)
        self.assertEqual(result, 436)  # add assertion here

    def test_solution2_result_on_example4(self):
        grid = parse_input("puzzle_input//d12_input_ex4.txt")
        result = solution_2(grid)
        self.assertEqual(result, 236)  # add assertion here

    def test_solution2_result_on_example5(self):
        grid = parse_input("puzzle_input//d12_input_ex5.txt")
        result = solution_2(grid)
        self.assertEqual(result, 368)  # add assertion here

if __name__ == '__main__':
    unittest.main()
