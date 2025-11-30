import unittest
from d9 import *

class Solution1Test(unittest.TestCase):
    def test_input_parsing_on_example(self):
        diskmap = parse_input("puzzle_input/d9_input_ex.txt")
        seeking = [ int(x) for x in '2333133121414131402']
        self.assertEqual(diskmap, seeking)

    def test_solution1_result_on_example(self):
        diskmap = parse_input("puzzle_input//d9_input_ex.txt")
        result = solution_1(diskmap)
        self.assertEqual(result, 1928)  # add assertion here


class Solution2Test(unittest.TestCase):
    def test_input_parsing_on_example(self):
        diskmap = parse_input("puzzle_input//d9_input_ex.txt")
        seeking = [ int(x) for x in '2333133121414131402']
        self.assertEqual(diskmap, seeking)

    def test_solution2_result_on_example(self):
        diskmap = parse_input("puzzle_input//d9_input_ex.txt")
        result = solution_2(diskmap)
        self.assertEqual(result, 2858)  # add assertion here

if __name__ == '__main__':
    unittest.main()
