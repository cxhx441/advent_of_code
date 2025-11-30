import unittest

from d20 import *

class SolutionTest(unittest.TestCase):
    # def test_input_parsing_on_example1(self):
    #     available, desired = parse_input("puzzle_input/d20_input_ex1.txt")
    #     self.assertEqual(['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br'], available)
    #     self.assertEqual(['brwrr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb'], desired)

    def test_solution1_parsing_on_example1(self):
        racetrack = parse_input("puzzle_input/d20_input_ex1.txt")
        stnd = best_wo_cheats(racetrack)
        self.assertEqual(84, stnd)

        total = solution_1(racetrack, 1)
        supposed2be = 14 + 14 + 2 + 4 + 2 + 3 + 1 + 1 + 1 + 1 + 1
        self.assertEqual(supposed2be, total)

    def test_solution2_parsing_on_example1(self):
        racetrack = parse_input("puzzle_input/d20_input_ex1.txt")
        total = solution_2(racetrack, 50)
        supposed2be = sum([32, 31, 29, 39, 25, 23, 20, 19, 12, 14, 12, 22, 4, 3])
        print(supposed2be, total)
        self.assertEqual(supposed2be, total)

if __name__ == '__main__':
    unittest.main()
