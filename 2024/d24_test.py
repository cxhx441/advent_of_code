import unittest
import math
from collections import defaultdict

from tabulate import tabulate

from d24 import *

class Solution1Test(unittest.TestCase):
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

    def test_solution1_on_real_input(self):
        nodes, nodes_and_gates, in_degrees, edges, q = parse_input("puzzle_input/d24_input.txt")
        result = solution_1(nodes, nodes_and_gates)
        self.assertEqual(result, 52728619468518)

class Solution2Test(unittest.TestCase):
    def test_solution2_on_ex3(self):
        CHOOSE = 4
        BITLIMIT = 6
        MASK = ( 1 << BITLIMIT) - 1
        nodes, nodes_and_gates, in_degrees, edges, q, z_target = parse_input2("puzzle_input/d24_input_ex3.txt")
        z_target = z_target & MASK
        z_target = 40 # bitwise and of x and y
        combos = itertools.combinations(in_degrees.keys(), CHOOSE)
        best = tuple()
        ngc = {k: v for k, v in nodes_and_gates.items()}
        n = {k: v for k, v in nodes.items()}
        original_sol = solution_1(n, ngc)
        print('og: ',original_sol)
        for combo in combos:
            perms = list(itertools.permutations(combo))
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

    def test_solution2_on_input(self):
        CHOOSE = 2
        BITLIMIT = 46
        MASK = ( 1 << BITLIMIT) - 1
        nodes, nodes_and_gates, in_degrees, edges, q, z_target = parse_input2("puzzle_input/d24_input_mod1.txt")
        sorted_in_degree_keys = sorted(in_degrees.keys())
        res_should_be = str(bin(z_target)[2:])

        ngc = {k: v for k, v in nodes_and_gates.items()}
        n = {k: v for k, v in nodes.items()}
        reverse_ngc = defaultdict(set)
        for k, v in ngc.items():
            n0, g, n1 = v
            reverse_ngc[(n0, n1)].add((k, g))
        for k, v in sorted(reverse_ngc.items()):
            print(k, v)


        # res_is = str(bin(solution_1(n, ngc))[2:])
        # i = 0
        # table = []
        # for k in sorted_in_degree_keys:
        #     row = []
        #     row.append(k)
        #     row.append(ngc[k])
        #     print(k, ngc[k], end=' ')
        #     if k[0] == 'z':
        #         print(res_should_be[i], end = ' ')
        #         print(res_is[i])
        #         row.append(res_should_be[i])
        #         row.append(res_is[i])
        #         i += 1
        #     else:
        #         row.append('')
        #         row.append('')
        #         print()
        #     table.append(row)
        # print(tabulate(table))
        # print(tabulate(table, headers=['k', 'ng', 'should_be', 'is']))

        z_target = z_target & MASK
        print('getting combos')
        print(math.comb(len(in_degrees.keys()), CHOOSE))
        pick_from = set(in_degrees.keys())
        pick_from.remove("z12")
        pick_from.remove("z19")
        pick_from.remove("z37")
        pick_from.remove("fgn")
        pick_from.remove("dck")
        pick_from.remove("qdg")
        combos = itertools.combinations(pick_from, CHOOSE)
        combo_count = math.comb(len(pick_from), CHOOSE)
        print('done combos')
        best = tuple()
        ngc = {k: v for k, v in nodes_and_gates.items()}
        n = {k: v for k, v in nodes.items()}
        original_sol = solution_1(n, ngc)
        print('og: ',original_sol)
        i = 0
        for combo in combos:
            combo = set(combo)
            combo.add("z19")
            combo.add("z37")
            combo.add("z12")
            combo.add("qdg")
            # combo.add("fgn")
            # combo.add("dck")
            i += 1
            perms = list(itertools.permutations(combo))
            perm_count = math.perm(len(combo))
            j = 0
            print(f'c: {i} / {combo_count}, p: {j} / {perm_count}')
            seen = set()
            for p in perms:
                if p in seen:
                    continue
                seen.add((
                   p[1], p[0],
                   p[3], p[2],
                   p[5], p[4]
                ))
                j += 1
                ngc = { k : v for k, v in nodes_and_gates.items() }
                n = { k : v for k, v in nodes.items() }
                # p = p + ("z12", "qdg")
                p = p + ("fgn", "dck")
                # print(ngc == nodes_and_gates)
                ngc[p[0]], ngc[p[1]] = ngc[p[1]], ngc[p[0]]
                ngc[p[2]], ngc[p[3]] = ngc[p[3]], ngc[p[2]]
                ngc[p[4]], ngc[p[5]] = ngc[p[5]], ngc[p[4]]
                ngc[p[6]], ngc[p[7]] = ngc[p[7]], ngc[p[6]]
                res = solution_1(n, ngc)
                if z_target == res:
                    best = p
                    best = sorted(best)
                    print('result: ', ','.join(best))
                    self.assertEqual(1, 1)
                    return 0
        self.assertEqual(0, 1)

    def test_solution2_on_input_again(self):
        CHOOSE = 8
        BITLIMIT = 46
        MASK = ( 1 << BITLIMIT) - 1
        nodes, nodes_and_gates, in_degrees, edges, q, z_target = parse_input2("puzzle_input/d24_input.txt")

        ngc = { k: (sorted(v)[1], sorted(v)[0], sorted(v)[2]) for k, v in nodes_and_gates.items()}
        output = []
        for k, v in ngc.items():
            output.append((k, v))
        output.sort()
        for v, k in output:
            print(v, k)

        print()
        output = []
        for v, k in ngc.items():
            output.append((k, v))
        output.sort()
        for k, v in output:
            print(k, v)


        return 0

if __name__ == '__main__':
    unittest.main()
