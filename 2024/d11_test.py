import unittest
from d11 import *

class Solution1Test(unittest.TestCase):
    def test_input_parsing_on_example(self):
        stones = parse_input("puzzle_input/d11_input_ex1.txt")
        seeking = [0,1,10,99,999]
        stones_list = stones.get_list()
        self.assertEqual(stones_list, seeking)

        stones = parse_input("puzzle_input/d11_input_ex2.txt")
        seeking = [125, 17]
        stones_list = stones.get_list()
        self.assertEqual(stones_list, seeking)

        stones = parse_input("puzzle_input/d11_input.txt")
        seeking = [17639,47,3858,0,470624,9467423,5,188]
        stones_list = stones.get_list()
        self.assertEqual(stones_list, seeking)

    def test_solution1_result_on_example1(self):
        stones = parse_input("puzzle_input//d11_input_ex1.txt")
        stones = blink(stones)
        result_list = stones.get_list()
        seeking = [1,2024,1,0,9,9,2021976]
        self.assertEqual(result_list, seeking)  # add assertion here
    #
    def test_solution1_result_on_example2(self):
        stones = parse_input("puzzle_input//d11_input_ex2.txt")
        result_list = stones.get_list()
        seeking0 = [125, 17]
        self.assertEqual(result_list, seeking0)  # add assertion here

        # 1
        stones = blink(stones)
        result_list = stones.get_list()
        seeking1 = [253000,1,7]
        self.assertEqual(result_list, seeking1)  # add assertion here

        # 2
        stones = blink(stones)
        result_list = stones.get_list()
        seeking2 = [253,0,2024,14168]
        self.assertEqual(result_list, seeking2)  # add assertion here

        # 3
        stones = blink(stones)
        result_list = stones.get_list()
        seeking3 = [512072,1,20,24,28676032]
        self.assertEqual(result_list, seeking3)  # add assertion here

        # 4
        stones = blink(stones)
        result_list = stones.get_list()
        seeking4 = [512,72,2024,2,0,2,4,2867,6032]
        self.assertEqual(result_list, seeking4)  # add assertion here

        # 5
        stones = blink(stones)
        result_list = stones.get_list()
        seeking5 = [1036288,7,2,20,24,4048,1,4048,8096,28,67,60,32]
        self.assertEqual(result_list, seeking5)  # add assertion here

        # 6
        stones = blink(stones)
        result_list = stones.get_list()
        seeking6 = [2097446912,14168,4048,2,0,2,4,40,48,2024,40,48,80,96,2,8,6,7,6,0,3,2]
        self.assertEqual(result_list, seeking6)  # add assertion here

        self.assertEqual(22, stones.count())

    def test_solution1_result_on_example2_count(self):
        stones = parse_input("puzzle_input//d11_input_ex2.txt")
        for _ in range(25):
            stones = blink(stones)
        self.assertEqual(55312, stones.count())



# class Solution2Test(unittest.TestCase):
#     def test_solution2_result_on_example(self):
#         stones = parse_input("puzzle_input//d11_input_ex2.txt")
#         result = solution_2(stones)
#         self.assertEqual(result, 81)  # add assertion here
    def test_solution2_on_example1(self):
        stones = parse_input("puzzle_input//d11_input_ex1.txt")
        count = solution_2(stones, 6)
        self.assertEqual(22, count)

if __name__ == '__main__':
    unittest.main()
