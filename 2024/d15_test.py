import unittest
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
    def test_solution2_result_on_example1(self):
        data = parse_input("puzzle_input//d15_input_ex1.txt")
        result = solution_2(data, 7, 11)
        print(result)
        rows, cols = 7, 11
        tree = get_tree1(rows, cols)
        print_tree(tree, only_have=True)

if __name__ == '__main__':
    unittest.main()
