import unittest

from d20 import *

class SolutionTest(unittest.TestCase):
    # def test_input_parsing_on_example1(self):
    #     available, desired = parse_input("puzzle_input/d20_input_ex1.txt")
    #     self.assertEqual(['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br'], available)
    #     self.assertEqual(['brwrr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb'], desired)

    def test_solution1_parsing_on_example1(self):
        racetrack = parse_input("puzzle_input/d20_input_ex1.txt")
        stnd, path = best_wo_cheats(racetrack)

        ROWS, COLS = len(racetrack), len(racetrack[0])
        print(len(path))
        path_set = set(path)
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in path_set:
                    racetrack[r][c] = "O"
        racetrack_strs = []
        for row in racetrack:
            racetrack_strs.append( ''.join( [ ch for ch in row ]) )

        for s in racetrack_strs:
            print(s)
        self.assertEqual(84, stnd)

    # def test_solution2_parsing_on_example1(self):
    #     available, desired = parse_input("puzzle_input/d20_input_ex1.txt")
    #     possible = solution_2(available, desired)
    #     self.assertEqual(16, possible)

if __name__ == '__main__':
    unittest.main()
