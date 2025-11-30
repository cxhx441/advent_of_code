import unittest
from gc import get_referrers

from d15 import *

class Solution1Test(unittest.TestCase):
    def test_input_parsing_on_example(self):
        grid, moves = parse_input("puzzle_input/d15_input_ex2.txt")
        self.assertEqual(grid[0][0], '#')
        self.assertEqual(grid[0][7], '#')
        self.assertEqual(grid[7][7], '#')
        self.assertEqual(grid[7][0], '#')
        self.assertEqual(grid[1][3], 'O')
        self.assertEqual(grid[2][2], '@')
        self.assertEqual(moves, '<^^>>>vv<v>>v<<')

    def test_solution1_result_on_example1(self):
        grid, moves = parse_input("puzzle_input//d15_input_ex1.txt")
        moves_should_be = '<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'
        self.assertEqual(moves, moves_should_be)
        result = solution_1(grid, moves)
        final_grid = [
            '##########',
            '#.O.O.OOO#',
            '#........#',
            '#OO......#',
            '#OO@.....#',
            '#O#.....O#',
            '#O.....OO#',
            '#O.....OO#',
            '#OO....OO#',
            '##########'
            ]
        grid_strs = []
        for r in range(len(grid)):
            grid_strs.append(''.join(grid[r]))

        self.assertEqual(final_grid, grid_strs)

        self.assertEqual(result, 10092)

    def test_solution1_result_on_example2(self):
        grid, moves = parse_input("puzzle_input//d15_input_ex2.txt")
        result = solution_1(grid, moves)
        self.assertEqual(result, 2028)

class Solution2Test(unittest.TestCase):
    def test_solution2_result_on_example2(self):
        grid, moves = parse_input("puzzle_input//d15_input_ex3.txt")
        upsized_grid = upsize_grid(grid)
        upsized_grid_should_be = ['##############',
                                  '##......##..##',
                                  '##..........##',
                                  '##....[][]@.##',
                                  '##....[]....##',
                                  '##..........##',
                                  '##############']
        print_grid(grid)
        print()
        print_grid(upsized_grid)
        upsized_grid_strs = []
        for r in range(len(grid)):
            upsized_grid_strs.append(''.join(upsized_grid[r]))
        self.assertEqual(upsized_grid_should_be, upsized_grid_strs)

    def test_solution2_result_on_example3(self):
        grid, moves = parse_input("puzzle_input//d15_input_ex3.txt")
        upsized_grid = upsize_grid(grid)
        result = solution_2(upsized_grid, moves)
        final_up_grid_should_be = [
            '##############',
            '##...[].##..##',
            '##...@.[]...##',
            '##....[]....##',
            '##..........##',
            '##..........##',
            '##############'
            ]

        grid_strs = []
        for r in range(len(upsized_grid)):
            grid_strs.append(''.join(upsized_grid[r]))
        self.assertEqual(final_up_grid_should_be, grid_strs)

    def test_solution2_result_on_example1(self):
        grid, moves = parse_input("puzzle_input//d15_input_ex1.txt")
        upsized_grid = upsize_grid(grid)
        result = solution_2(upsized_grid, moves)
        finall = ['####################',
        '##[].......[].[][]##',
        '##[]...........[].##',
        '##[]........[][][]##',
        '##[]......[]....[]##',
        '##..##......[]....##',
        '##..[]............##',
        '##..@......[].[][]##',
        '##......[][]..[]..##',
        '####################']
        grid_strs = []
        for r in range(len(upsized_grid)):
            grid_strs.append(''.join(upsized_grid[r]))
        print_grid(upsized_grid)
        print_grid(finall)
        # self.assertEqual(finall, upsized_grid)

        self.assertEqual(result, 9021)

    def test_solution2_result_on_customexample1(self):
        upgrid = [ ['#','#','#','#'],
                   ['#','.','.','#'],
                   ['#','[',']','#'],
                   ['#','[',']','#'],
                   ['#','@','.','#'],
                   ['#','#','#','#']]
        moves = '^^'
        final_should_be = [ ['#','#','#', '#'],
                            ['#','[',']','#'],
                            ['#','[',']','#'],
                            ['#','@','.','#'],
                            ['#','.','.','#'],
                            ['#','#','#','#']]

        result = solution_2(upgrid, moves)
        self.assertEqual(final_should_be, upgrid)

    def test_solution2_result_on_customexample2(self):
        upgrid = [ ['#','#','#','#'],
                   ['#','.','.','#'],
                   ['#','[',']','#'],
                   ['#','[',']','#'],
                   ['#','.','@','#'],
                   ['#','#','#','#']]
        moves = '^^'
        final_should_be = [ ['#','#','#', '#'],
                            ['#','[',']','#'],
                            ['#','[',']','#'],
                            ['#','.','@','#'],
                            ['#','.','.','#'],
                            ['#','#','#','#']]

        result = solution_2(upgrid, moves)
        self.assertEqual(final_should_be, upgrid)

    def test_solution2_result_on_customexample3(self):
        upgrid = [ ['#','#','#','#'],
                   ['#','.','@','#'],
                   ['#','[',']','#'],
                   ['#','[',']','#'],
                   ['#','.','.','#'],
                   ['#','#','#','#']]
        moves = 'vv'
        final_should_be = [ ['#','#','#', '#'],
                            ['#','.','.','#'],
                            ['#','.','@','#'],
                            ['#','[',']','#'],
                            ['#','[',']','#'],
                            ['#','#','#','#']]

        result = solution_2(upgrid, moves)
        self.assertEqual(final_should_be, upgrid)

    def test_solution2_result_on_customexample5(self):
        upgrid = [ ['#','#','#','#','#','#'],
                   ['#','@','.','.','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','.','[',']','.','#'],
                   ['#','.','.','[',']','#'],
                   ['#','.','.','.','.','#'],
                   ['#','.','.','.','.','#'],
                   ['#','.','.','.','.','#'],
                   ['#','#','#','#','#','#']]
        moves = 'vvvvv'
        finall = [ ['#','#','#','#','#','#'],
                   ['#','.','.','.','.','#'],
                   ['#','.','.','.','.','#'],
                   ['#','.','.','.','.','#'],
                   ['#','@','.','.','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','.','[',']','.','#'],
                   ['#','.','.','[',']','#'],
                   ['#','#','#','#','#','#']]
        result = solution_2(upgrid, moves)
        self.assertEqual(finall, upgrid)

    def test_solution2_result_on_customexample5(self):
        upgrid = [ ['#','#','#','#','#','#'],
                   ['#','@','.','.','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','.','[',']','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','.','[',']','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','.','.','.','.','#'],
                   ['#','#','#','#','#','#']]
        moves = 'vvvvv'
        finall = [ ['#','#','#','#','#','#'],
                   ['#','.','.','.','.','#'],
                   ['#','@','.','.','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','.','[',']','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','.','[',']','.','#'],
                   ['#','[',']','.','.','#'],
                   ['#','#','#','#','#','#']]
        result = solution_2(upgrid, moves)
        self.assertEqual(finall, upgrid)

    def test_solution2_result_on_customexample6(self):
        upgrid = [
            list('####################################################################################################'),
            list('##[][].................@......##.[]...[].[]...............[][].[].[]..[][]....[]..[]....##..##[][]##'),
            list('##[][]..##........##..[]##....##[]....[]........##...[][].[][].[][][].......##..[]............[]..##'),
            list('##..##...[][].........[][].....[]...........##[][][]..[]##[][]..[]................##[]..##..##[]####'),
            list('##....[]##[][][][]...[][][].......[]............[][][][]..[]....[].[]...[].........[][][].......[]##'),
            list('##......[]##.[].[]....[][]............##[].......[][]...##[].......[].....##......[]..[]....[]....##'),
            list('##.[].....[][][].[].[][][]........[][][]................##.......[]......[]...[]......##..........##'),
            list('####........[][]##[].[].................##.......[].[]................[][][]...[]...##........[]..##'),
            list('##[]...........[].[]..................[]........[][]..................##[]......[]......[]..[]....##'),
            list('##[]..........##..[]..........[]..##..[]..........[][][]............[][].......[].......##........##'),
            list('####################################################################################################'),
            ]


        moves = 'v'
        finall = [
            list('####################################################################################################'),
            list('##[][]........................##.[]...[].[]...............[][].[].[]..[][]....[]..[]....##..##[][]##'),
            list('##[][]..##........##...@##....##[]....[]........##...[][].[][].[][][].......##..[]............[]..##'),
            list('##..##...[][].........[][].....[]...........##[][][]..[]##[][]..[]................##[]..##..##[]####'),
            list('##....[]##[][][][]....[].[].......[]............[][][][]..[]....[].[]...[].........[][][].......[]##'),
            list('##......[]##.[].[]...[][].............##[].......[][]...##[].......[].....##......[]..[]....[]....##'),
            list('##.[].....[][][].[].[][][]........[][][]................##.......[]......[]...[]......##..........##'),
            list('####........[][]##[]..[][]..............##.......[].[]................[][][]...[]...##........[]..##'),
            list('##[]...........[].[].[]...............[]........[][]..................##[]......[]......[]..[]....##'),
            list('##[]..........##..[]..........[]..##..[]..........[][][]............[][].......[].......##........##'),
            list('####################################################################################################'),
        ]
        result = solution_2(upgrid, moves)
        self.assertEqual(finall, upgrid)









if __name__ == '__main__':
    unittest.main()
