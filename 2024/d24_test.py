import unittest
import math

from d24 import *

class SolutionTest(unittest.TestCase):
    def test_input_parsing_on_example1(self):
        x = parse_input("puzzle_input/d24_input_ex1.txt")
        self.assertEqual(1, 1)

    def test_solution1_on_ex1(self):
        nodes, nodes_and_gates, in_degrees, edges, q = parse_input("puzzle_input/d24_input_ex1.txt")
        result = solution_1(nodes, nodes_and_gates)
        self.assertEqual(result, 4)

    def test_solution1_on_ex2(self):
        nodes, nodes_and_gates, in_degrees, edges, q = parse_input("puzzle_input/d24_input_ex2.txt")
        result = solution_1(nodes, nodes_and_gates)
        self.assertEqual(result, 2024)

    def test_solution2_on_ex3(self):
        CHOOSE = 4
        BITLIMIT = 6
        MASK = ( 1 << BITLIMIT) - 1
        nodes, nodes_and_gates, in_degrees, edges, q, z_target = parse_input2("puzzle_input/d24_input_ex3.txt")
        z_target = z_target & MASK
        combos = list(itertools.combinations(in_degrees.keys(), CHOOSE))
        best = tuple()
        for combo in combos:
            perms = list(itertools.permutations(combo))
            ngc = {k: v for k, v in nodes_and_gates.items()}
            n = {k: v for k, v in nodes.items()}
            original_sol = solution_1(n, ngc)
            print(original_sol)
            for p in perms:
                ngc = { k : v for k, v in nodes_and_gates.items() }
                n = { k : v for k, v in nodes.items() }
                # print(ngc == nodes_and_gates)
                ngc[p[0]], ngc[p[1]] = ngc[p[1]], ngc[p[0]]
                ngc[p[2]], ngc[p[3]] = ngc[p[3]], ngc[p[2]]
                # print(ngc == nodes_and_gates)
                # ngc[combo[4]], ngc[combo[5]] = ngc[combo[5]], ngc[combo[4]]
                # ngc[combo[6]], ngc[combo[7]] = ngc[combo[7]], ngc[combo[6]]
                res = solution_1(n, ngc)
                print(res)
                if z_target == res:
                    best = combo
                    best = sorted(best)
                    self.assertEqual(','.join(best), 'z00,z01,z02,z05')
                    return
        self.assertEqual(0, 1)


if __name__ == '__main__':
    unittest.main()
