import unittest

from d20 import *

class SolutionTest(unittest.TestCase):
    def test_input_parsing_on_example1(self):
        available, desired = parse_input("puzzle_input/d20_input_ex1.txt")
        self.assertEqual(['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br'], available)
        self.assertEqual(['brwrr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb'], desired)

    # def test_solution1_parsing_on_example1(self):
    #     available, desired = parse_input("puzzle_input/d20_input_ex1.txt")
    #     possible = solution_1(available, desired)
    #     self.assertEqual(6, possible)
    #
    # def test_solution2_parsing_on_example1(self):
    #     available, desired = parse_input("puzzle_input/d20_input_ex1.txt")
    #     possible = solution_2(available, desired)
    #     self.assertEqual(16, possible)

if __name__ == '__main__':
    unittest.main()
