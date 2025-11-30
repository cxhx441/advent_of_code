from timeit import default_timer as timer
import collections

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        nums = []
        for line in f:
            nums.append(int(line.strip()))
    return nums


def next_secret_num(secret_num):
    '''

    Calculate the result of multiplying the secret number by 64.
        Then, mix this result into the secret number.
        Finally, prune the secret number.
    Calculate the result of dividing the secret number by 32.
        Round the result down to the nearest integer.
        Then, mix this result into the secret number.
        Finally, prune the secret number.
    Calculate the result of multiplying the secret number by 2048.
        Then, mix this result into the secret number.
        Finally, prune the secret number.

    To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
    To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
    '''
    res = secret_num * 64
    secret_num = secret_num ^ res  # mix
    secret_num = secret_num % 16777216  # prune

    res = secret_num // 32
    secret_num = secret_num ^ res  # mix
    secret_num = secret_num % 16777216  # prune

    res = secret_num * 2048
    secret_num = secret_num ^ res  # mix
    secret_num = secret_num % 16777216  # prune

    return secret_num

def solution_1(nums, count):

    secret_nums = []
    for n in nums:
        for _ in range(count):
            n = next_secret_num(n)

        secret_nums.append(n)

    return sum(secret_nums)


def solution_2(starting_nums, count):
    n = len(starting_nums)

    # get starting nums
    secret_nums = [[x] for x in starting_nums]
    for i, monkeys_secret_nums in enumerate(secret_nums):
        for _ in range(count):
            nxt = next_secret_num(monkeys_secret_nums[-1])
            monkeys_secret_nums.append(nxt)

    # get prices
    prices = [ [ x % 10 for x in monkeys_secret_nums ] for monkeys_secret_nums in secret_nums ]

    # get price changes
    price_changes = [ [None] for _ in range(n) ]
    prev = None
    for i in range(n):
        monkeys_price_changes = price_changes[i]
        monkeys_prices = prices[i]
        for j, price in enumerate(monkeys_prices):
            if j == 0:
                prev = price
            else:
                tmp = price
                monkeys_price_changes.append(price - prev)
                prev = tmp

    # get 4 sequence sums
    sequence_dics = [ dict() for _ in range(n) ]
    unique_sequences = dict()
    for i, monkeys_price_changes in enumerate(price_changes):
        d = sequence_dics[i]
        for j in range(1, len(monkeys_price_changes) - 3):
            sequence = tuple(monkeys_price_changes[j: j + 4])
            if sequence not in d:
                d[sequence] = prices[i][j + 4 - 1]
            unique_sequences[sequence] = 0

    # get max
    max_res = 0
    best_sequence = None
    for sequence in unique_sequences:
        sequence_total = 0
        for d in sequence_dics:
            unique_sequences[sequence] += d.get(sequence, 0)

    mx = 0
    bst = None
    for k, v in unique_sequences.items():
        # print(k, v)
        if v > mx:
            mx = max(mx, v)
            bst = v

    # for i in range(n):
        # print(sequence_dics[i][(-2, 1, -1, 3)])
        # print(sequence_dics[i][(0, 6, -4, 4)])
    print(bst)
    return mx


if __name__ == "__main__":
    # start = timer()
    # nums = parse_input("puzzle_input/d22_input.txt")
    # total = solution_1(nums, 2000)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution1: {total}')

    start = timer()
    # nums = parse_input("puzzle_input/d22_input_ex2.txt")
    nums = parse_input("puzzle_input/d22_input.txt")
    max_bananas = solution_2(nums, 2000)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution2: {max_bananas}')

