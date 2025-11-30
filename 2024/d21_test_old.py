import unittest

from d21 import *

class SolutionTest(unittest.TestCase):
    def test_input_parsing_on_example1(self):
        codes = parse_input("puzzle_input/d21_input_ex1.txt")
        self.assertEqual(codes[0], '029A')
        self.assertEqual(codes[4], '379A')


    def test_can_input_to_get_correct_codes(self):
        A_h = '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'
        A_r0 = 'v<<A>>^A<A>AvA<^AA>A<vAAA>^A'
        A_r1 = '<A^A>^^AvvvA'
        A_k = '029A'

        dpad_R0 = Dpad()
        dpad_R1 = Dpad()
        keypad = Keypad()


        for i, ch in enumerate(A_h):
            dpad_R0.send(ch)
        self.assertEqual( ''.join(dpad_R0.pressed_keys), A_r0 )

        for ch in dpad_R0.pressed_keys:
            dpad_R1.send(ch)
        self.assertEqual( ''.join(dpad_R1.pressed_keys), A_r1 )

        for ch in dpad_R1.pressed_keys:
            keypad.send(ch)
        self.assertEqual( ''.join(keypad.pressed_keys), A_k )

    def test_solution1_parsing_on_example1(self):
        codes = parse_input("puzzle_input/d21_input_ex1.txt")
        complexity = solution_1(codes)
        self.assertEqual(126384, complexity)

if __name__ == '__main__':
    unittest.main()
