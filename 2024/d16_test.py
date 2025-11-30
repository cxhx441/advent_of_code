import unittest
from gc import get_referrers

from d16 import *

class Solution1Test(unittest.TestCase):
    # def test_input_parsing_on_example(self):
    def test_solution1_result_on_example1(self):
        maze = parse_input("puzzle_input/d16_input_ex1.txt")
        result = solution_1(maze)
        self.assertEqual(result, 7036)

    def test_solution1_result_on_example2(self):
        maze = parse_input("puzzle_input/d16_input_ex2.txt")
        result = solution_1(maze)
        self.assertEqual(result, 11048)

class Solution2Test(unittest.TestCase):
    # def test_input_parsing_on_example(self):
    def test_result_on_example1(self):
        maze = parse_input("puzzle_input/d16_input_ex1.txt")
        result = solution_2(maze)
        self.assertEqual(45, result)

    def test_result_on_example2(self):
        maze = parse_input("puzzle_input/d16_input_ex2.txt")
        result = solution_2(maze)
        self.assertEqual(64, result)


if __name__ == '__main__':
    unittest.main()
