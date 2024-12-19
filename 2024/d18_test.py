import unittest

from d18 import *

class SolutionTest(unittest.TestCase):
    def test_input_parsing_on_example1(self):
        grid, bytes = parse_input("puzzle_input/d18_input_ex1.txt", 6)
        grid_should_be = [
                        '...#...',
                        '..#..#.',
                        '....#..',
                        '...#..#',
                        '..#..#.',
                        '.#..#..',
                        '#.#....'
        ]

        drop(grid, bytes, 12)
        grid = [ ''.join([ch for ch in x]) for x in grid]

        self.assertEqual(grid_should_be, grid)

    def test_solution1_parsing_on_example1(self):
        grid, bytes = parse_input("puzzle_input/d18_input_ex1.txt", 6)
        steps = solution_1(grid, bytes, 12)
        self.assertEqual(steps, 22)

    def test_solution2_parsing_on_example1(self):
        grid, bytes = parse_input("puzzle_input/d18_input_ex1.txt", 6)
        coord = solution_2(grid, bytes)
        self.assertEqual((6, 1), coord)

if __name__ == '__main__':
    unittest.main()
