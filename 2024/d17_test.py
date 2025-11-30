import unittest

from d17 import *

class SolutionTest(unittest.TestCase):
    def test_input_parsing_on_example(self):
        db = parse_input("puzzle_input/d17_input_ex1.txt")
        self.assertEqual(db.a, 729)
        self.assertEqual(db.b, 0)
        self.assertEqual(db.c, 0)
        self.assertEqual(db.program, [0,1,5,4,3,0])


    def test_solution1_result_on_example1(self):
        db = parse_input("puzzle_input/d17_input_ex1.txt")
        db.run()
        self.assertEqual(db.get_output(), '4,6,3,5,6,3,5,2,1,0')

    def test_solution2_result_on_example2(self):
        result = solution_2("puzzle_input//d17_input_ex2.txt")
        self.assertEqual(result, 117440)

#
#     def test_solution1_result_on_example2(self):
#         maze = parse_input("puzzle_input/d16_input_ex2.txt")
#         result = solution_1(maze)
#         self.assertEqual(result, 11048)
#
# class Solution2Test(unittest.TestCase):
#     # def test_input_parsing_on_example(self):
#     def test_result_on_example1(self):
#         maze = parse_input("puzzle_input/d16_input_ex1.txt")
#         result = solution_2(maze)
#         self.assertEqual(45, result)
#
#     def test_result_on_example2(self):
#         maze = parse_input("puzzle_input/d16_input_ex2.txt")
#         result = solution_2(maze)
#         self.assertEqual(64, result)
#

if __name__ == '__main__':
    unittest.main()
