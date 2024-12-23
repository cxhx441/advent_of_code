import unittest

from d23 import *

class SolutionTest(unittest.TestCase):
    def test_input_parsing_on_example1(self):
        nodes, edges = parse_input("puzzle_input/d23_input_ex1.txt")
        self.assertEqual(1, 1)

    def test_solution1_on_ex1(self):
        edges = parse_input("puzzle_input/d23_input_ex1.txt")
        tees = solution_1(edges)
        A_tees = {
            ('co', 'de', 'ta'),
            ('co', 'ka', 'ta'),
            ('de', 'ka', 'ta'),
            ('qp', 'td', 'wh'),
            ('tb', 'vc', 'wq'),
            ('tc', 'td', 'wh'),
            ('td', 'wh', 'yn')
        }
        self.assertEqual(A_tees, tees)


    def test_solution2_on_ex1(self):
        edges = parse_input("puzzle_input/d23_input_ex1.txt")
        best = solution_2(edges)
        self.assertEqual({'co','de','ka','ta'}, best)

   #     self.assertEqual(max_bananas, 6)


if __name__ == '__main__':
    unittest.main()
