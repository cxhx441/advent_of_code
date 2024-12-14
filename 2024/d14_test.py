import unittest
from d14 import *

class Solution1Test(unittest.TestCase):
    def test_input_parsing_on_example(self):
        data = parse_input("puzzle_input/d14_input_ex1.txt")
        self.assertEqual(data[10]["p"], [2, 4])
        self.assertEqual(data[10]["v"], [2, -3])


    def test_solution1_result_on_example1(self):
        data = parse_input("puzzle_input//d14_input_ex1.txt")
        result = solution_1(data, 7, 11, 100)
        self.assertEqual(result, 12)  # add assertion here

        data = parse_input("puzzle_input//d14_input.txt")
        result = solution_1(data, 103, 101, 100)
        self.assertEqual(result, 229980828)  # add assertion here

class Solution2Test(unittest.TestCase):
    def test_solution2_result_on_example1(self):
        data = parse_input("puzzle_input//d14_input_ex1.txt")
        result = solution_2(data, 7, 11)
        print(result)
        rows, cols = 7, 11
        tree = get_tree1(rows, cols)
        print_tree(tree, only_have=True)

if __name__ == '__main__':
    unittest.main()
