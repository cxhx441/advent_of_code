import collections
from timeit import default_timer as timer
class Node:
    def __init__(self, val, prev=None, next=None, blinked=0):
        self.val = val
        # self.prev = prev
        self.next = next
        self.blinked = blinked

    def __repr__(self):
        vals = self.get_list()
        chars = [ str(x) if x is not None else None for x in vals ]
        return ", ".join(chars)

    def get_list(self):
        cur = self
        vals = []
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals

    def sum(self):
        cur = self
        total = 0
        while cur:
            total += cur.val
            cur = cur.next
        return total

    def count(self):
        cur = self
        total = 0
        while cur:
            total += 1
            cur = cur.next
        return total



def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        sentinel = Node(None)
        for line in f:
            prev = None
            cur = sentinel
            for num in line[:-1].split(" "):
                new_node = Node(int(num))
                cur.next = new_node
                new_node.prev = cur
                cur = new_node
            break
    return sentinel.next


def blink(stone):
    cur = stone
    while cur:
        val = cur.val
        if val == 0: # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
            cur.val = 1
        elif len(str(val)) % 2 == 0: # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.(The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            tmp = cur.next

            str_val = str(val)
            len_val = len(str_val)
            half_len = len_val // 2

            left = str_val[:half_len]
            cur.val = int( left )

            right = str_val[half_len: ].lstrip('0')
            if right == '': right = '0'
            cur.next = Node( int( right ) )

            cur = cur.next
            cur.next = tmp
        else: # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
            cur.val *= 2024
        cur = cur.next
    return stone

def solution_1(stones):
    for _ in range(25):
        blink(stones)
    return stones.count()

def solution_2(stones, blink_count):
    stone_counts = collections.defaultdict(int)

    cur = stones
    stones_list = []
    while cur:
        stones_list.append( cur.val )
        cur = cur.next

    for s in stones_list:
        stone_counts[s] += 1

    for i in range(blink_count):
        copy_stone_counts = stone_counts.copy()
        for stone, count in copy_stone_counts.items():
            stone_counts[stone] -= count
            new_stones = blink(Node(stone)).get_list()
            for new_stone in new_stones:
                stone_counts[new_stone] += count

    total = sum(stone_counts.values())
    return total

if __name__ == '__main__':
    start = timer()
    stones = parse_input("puzzle_input//d11_input.txt")
    result = solution_1(stones)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')

    start = timer()
    stones = parse_input("puzzle_input//d11_input.txt")
    result = solution_2(stones, 75)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution2: {result}')
