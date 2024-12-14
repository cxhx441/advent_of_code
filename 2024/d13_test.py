import unittest
from d13 import *

class Solution1Test(unittest.TestCase):
    def test_input_parsing_on_example(self):
        machines = parse_input("puzzle_input/d13_input_ex1.txt")
        self.assertEqual(len(machines), 4)
        self.assertEqual(machines[-1].Ax, 69)


    def test_solution1_result_on_example1(self):
        machines = parse_input("puzzle_input//d13_input_ex1.txt")
        self.assertEqual(machines[0].get_cost(), 280)  # add assertion here
        self.assertEqual(machines[1].get_cost(), 0)  # add assertion here
        self.assertEqual(machines[2].get_cost(), 200)  # add assertion here
        self.assertEqual(machines[3].get_cost(), 0)  # add assertion here

        result = solution_1(machines)
        self.assertEqual(result, 480)  # add assertion here

    def test_solution1_result_on_example2(self):
        machines = parse_input("puzzle_input//d13_input_ex2.txt")
        self.assertEqual(machines[0].get_cost(), 100)  # add assertion here
        self.assertEqual(machines[1].get_cost(), 300)  # add assertion here
        # self.assertEqual(machines[0].get_cost(), 300)  # add assertion here
        # self.assertEqual(machines[1].get_cost(), 300)  # add assertion here
        # self.assertEqual(machines[2].get_cost(), 100)  # add assertion here
        # self.assertEqual(machines[3].get_cost(), 100)  # add assertion here
        #
        result = solution_1(machines)
        self.assertEqual(result, 400)  # add assertion here

class Solution2Test(unittest.TestCase):
    def test_solution2_result_on_example1(self):
        machines = parse_input("puzzle_input//d13_input_ex1.txt")
        self.assertEqual(machines[0].get_cost2(), 280)  # add assertion here
        self.assertEqual(machines[1].get_cost2(), 0)  # add assertion here
        self.assertEqual(machines[2].get_cost2(), 200)  # add assertion here
        self.assertEqual(machines[3].get_cost2(), 0)  # add assertion here

        self.assertEqual(machines[0].get_cost2(w_error=True), 0)  # add assertion here
        self.assertEqual(machines[2].get_cost2(w_error=True), 0)  # add assertion here

        # result = solution_2(machines)
        # self.assertEqual(result, 480)  # add assertion here

    # def test_solution1_result_on_example2(self):
    #     machines = parse_input("puzzle_input//d13_input_ex2.txt")
    #     self.assertEqual(machines[0].get_cost(), 100)  # add assertion here
    #     self.assertEqual(machines[1].get_cost(), 300)  # add assertion here
    #     # self.assertEqual(machines[0].get_cost(), 300)  # add assertion here
    #     # self.assertEqual(machines[1].get_cost(), 300)  # add assertion here
    #     # self.assertEqual(machines[2].get_cost(), 100)  # add assertion here
    #     # self.assertEqual(machines[3].get_cost(), 100)  # add assertion here
    #     #
    #     result = solution_2(machines)
    #     self.assertEqual(result, 400)  # add assertion here

if __name__ == '__main__':
    unittest.main()
