from timeit import default_timer as timer
import collections

class Pad:
    def __init__(self):
        self.pos = []
        self.keys = [[]]
        self.ROWS, self.COLS = len(self.keys), len(self.keys[0])
        self.invalid_pos = [0, 0]
        self.pressed_keys = []
        self.key_to_coord = {}

    def is_invalid_pos(self):
        r, c = self.pos
        if not ( 0 <= r < self.ROWS or 0 <= c < self.COLS) or self.pos == self.invalid_pos:
            return True
        return False

    def _mv_right(self):
        r, c = self.pos
        self.pos[0], self.pos[1] = r, c + 1
        if self.is_invalid_pos():
            raise IndexError

    def _mv_down(self):
        r, c = self.pos
        self.pos[0], self.pos[1] = r + 1, c
        if self.is_invalid_pos():
            raise IndexError

    def _mv_left(self):
        r, c = self.pos
        self.pos[0], self.pos[1] = r, c - 1
        if self.is_invalid_pos():
            raise IndexError

    def _mv_up(self):
        r, c = self.pos
        self.pos[0], self.pos[1] = r - 1, c
        if self.is_invalid_pos():
            raise IndexError

    def send(self, ch):
        if ch == '>':
            self._mv_right()
        elif ch == 'v':
            self._mv_down()
        elif ch == '<':
            self._mv_left()
        elif ch == '^':
            self._mv_up()
        elif ch == 'A':
            self.press()
        else:
            raise ValueError

    def press(self):
        r, c = self.pos
        pressed_key = self.keys[r][c]
        self.pressed_keys.append(pressed_key)
        return pressed_key


class Keypad(Pad):
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """

    def __init__(self):
        super().__init__()
        self.pos = [3, 2]
        self.keys = [ ['7', '8', '9'],
                      ['4', '5', '6'],
                      ['1', '2', '3'],
             [float("inf"), '0', 'A']]
        self.ROWS, self.COLS = len(self.keys), len(self.keys[0])
        self.invalid_pos = [3, 0]
        self.key_to_coord = {}
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if [r, c] == self.invalid_pos:
                    continue
                self.key_to_coord[self.keys[r][c]] = (r, c)


class Dpad(Pad):
    """
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    """

    def __init__(self):
        super().__init__()
        self.pos = [0, 2]
        self.keys = [ [float("inf"), '^', 'A'],
                      ['<', 'v', '>'] ]
        self.ROWS, self.COLS = len(self.keys), len(self.keys[0])
        self.invalid_pos = [0, 0]
        self.key_to_coord = {}
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if [r, c] == self.invalid_pos:
                    continue
                self.key_to_coord[self.keys[r][c]] = (r, c)


def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        codes = []
        for line in f:
            codes.append(line.strip())
    return codes


def solution_1(codes):
    def get_sequence(prev, target, dir_dic, pad):
        if (prev, target) in dir_dic:
            return dir_dic[(prev, target)]

        start = pad.key_to_coord[prev]
        q = collections.deque( [ (*start, [] ) ] )
        seen = set()
        while q:
            r, c, sequence = q.popleft()
            if not ( 0 <= r < pad.ROWS or 0 <= c < pad.COLS) or [r, c] == pad.invalid_pos:
                continue
            if (r, c) in seen:
                continue
            seen.add((r, c))
            if (r, c) == pad.key_to_coord[target]:
                pad.pos = list(pad.key_to_coord[prev])
                sequence.sort()
                try:
                    for ch in sequence:
                        pad.send(ch)
                except IndexError:
                    print('IndexError')
                    sequence.sort(reverse=True)
                # dir_dic[(prev, target)] = sequence.copy()
                return sequence

            for dr, dc, dir in [
                                (0, 1, '>'),
                                (1, 0, 'v'),
                                (0, -1, '<'),
                                (-1, 0, '^')
            ]:
                nr, nc = r + dr, c + dc
                q.append((nr, nc, sequence + [dir]))

    keypad_dir = {}
    dpad_dir = {}
    prev_k = 'A'
    prev_r1 = 'A'
    prev_r0 = 'A'
    def get_human_input(code):
        """ hk -> r0 -> r1 """
        nonlocal prev_k, prev_r1, prev_r0

        print(code)
        r1_sequence = []
        for i, target in enumerate(code):
            sub_seq = get_sequence(prev_k, target, keypad_dir, Keypad())
            r1_sequence.extend(sub_seq)
            r1_sequence.append('A')
            prev_k = target
        r1_sequence = ''.join(r1_sequence)
        print(r1_sequence)

        r0_sequence = []
        for i, target in enumerate(r1_sequence):
            sub_seq = get_sequence(prev_r1, target, dpad_dir, Dpad())
            r0_sequence.extend(sub_seq)
            r0_sequence.append('A')
            prev_r1 = target
        r0_sequence = ''.join(r0_sequence)
        print(r0_sequence)

        h_sequence = []
        for target in r0_sequence:
            sub_seq = get_sequence(prev_r0, target, dpad_dir, Dpad())
            h_sequence.extend(sub_seq)
            h_sequence.append('A')
            prev_r0 = target
        h_sequence = ''.join(h_sequence)
        print(h_sequence)
        print()
        return h_sequence

    h_inputs = []
    for code in codes:
        h_input = get_human_input(code)
        h_inputs.append(h_input)

    print()
    for h in h_inputs:
        print(h)

    complexities = []
    for code, h_input in zip(codes, h_inputs):
        num = int( code.lstrip('0')[:-1] )
        l = len(h_input)
        complexities.append( num * l)

    return sum(complexities)

def solution_2():
    return 0


if __name__ == "__main__":
    start = timer()
    codes = parse_input("puzzle_input/d21_input.txt")
    complexity = solution_1(codes)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {complexity}')

    # start = timer()
    # racetrack = parse_input("puzzle_input/d20_input.txt")
    # result = solution_2(racetrack, 100)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution1: {result}')

