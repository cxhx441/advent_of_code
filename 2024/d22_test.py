import unittest

from d22 import *

class SolutionTest(unittest.TestCase):
    def test_input_parsing_on_example1(self):
        nums = parse_input("puzzle_input/d22_input_ex1.txt")
        self.assertEqual(1, 1)

    def test_next_secret_nums(self):
        A_secret_nums = [123,
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254]

        secret_nums = [123]
        print(secret_nums[-1])
        for _ in range(10):
            secret_nums.append(next_secret_num(secret_nums[-1]))
            print(secret_nums[-1])
        self.assertEqual(secret_nums, A_secret_nums)

    def test_solution1_on_ex1(self):
        nums = parse_input("puzzle_input/d22_input_ex1.txt")

        A_sn = [8685429, 4700978, 15273692, 8667524]

        a0 = solution_1([nums[0]], 2000)
        self.assertEqual(A_sn[0], a0)

        a1 = solution_1([nums[1]], 2000)
        self.assertEqual(A_sn[1], a1)

        a2 = solution_1([nums[2]], 2000)
        self.assertEqual(A_sn[2], a2)

        a3 = solution_1([nums[3]], 2000)
        self.assertEqual(A_sn[3], a3)


        total = solution_1(nums, 2000)
        self.assertEqual(sum(A_sn), total)

    def test_solution2_on_text_ex(self):
        max_bananas = solution_2([123], 9)
        self.assertEqual(max_bananas, 6)

    def test_solution2_on_ex2(self):
        nums = parse_input("puzzle_input/d22_input_ex2.txt")
        # max_bananas = solution_2([nums[3]], 2000)
        max_bananas = solution_2(nums, 2000)
        self.assertEqual(max_bananas, 23)



if __name__ == '__main__':
    unittest.main()
