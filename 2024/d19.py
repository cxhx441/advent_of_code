from timeit import default_timer as timer
import heapq

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        data = f.read().strip()
        available, desired = data.split('\n\n')
        available = available.split(', ')
        desired = desired.split('\n')
    return available, desired

def solution_1(available, desired):
    available = set(available)
    possible = 0

    def backtrack(first, d):
        if first == len(d):
            return True

        for i in range(1, len(d) - first + 1):
            cur = d[first : first + i]
            if cur not in available:
                continue
            if backtrack(first + i, d):
                return True

        return False

    for d in desired:
        if backtrack(0, d):
            possible += 1
    return possible


# def solution_2(available, desired):
#     # dp = {pattern : ways_to_create}
#
#     desired = {d: 0 for d in desired}
#     # available = set(available)
#     max_len_d = max(len(d) for d in desired)
#
#     def backtrack(path, n):
#         print(path)
#         if n > max_len_d:
#             return
#
#         w = ''.join(path)
#         if w in desired:
#             desired[w] += 1
#
#         for a in available:
#             n += len(a)
#             path.append(a)
#             backtrack(path, n)
#             n -= len(a)
#             path.pop()
#
#         return False
#
#     backtrack([], 0)
#     return sum(desired.values())


def solution_2(available, desired):
    memo = {}
    def backtrack(prefix):
        if prefix == '':
            return 1

        if prefix in memo:
            return memo[prefix]

        count = 0
        for a in available:
            if prefix.startswith(a):
                count += backtrack(prefix[len(a):])
        memo[prefix] = count
        return count

    total = 0
    for d in desired:
        total += backtrack(d)
    return total




















    # def backtrack(target):
    #     if not target:
    #         return 1
    #
    #     if target in memo:
    #         return memo[target]
    #
    #     these_ways = 0
    #     for s in available:
    #         if target.startswith(s):
    #             these_ways += backtrack(target[len(s):])
    #     memo[target] = these_ways
    #     return these_ways
    #
    # memo = dict()
    # total_ways = 0
    # for d in desired:
    #     print(d)
    #     total_ways += backtrack(d)
    # return total_ways
    #

    # available = set(available)
    # possible = 0
    # max_len_d = max(len(d) for d in desired)
    #
    # def backtrack(first, d, path):
    #     w = ''.join(path)
    #     if len(w) > max_len_d:
    #         return
    #     if len(w) == lend
    #     nonlocal possible
    #     if first == len(d):
    #         print(possible)
    #         possible += 1
    #
    #     for i in range(1, len(d) - first + 1):
    #         cur = d[first : first + i]
    #         if cur not in available:
    #             continue
    #         if backtrack(first + i, d):
    #             return True
    #
    #     return False
    #
    # for i, d in enumerate(desired):
    #     print(i, len(d))
    #     backtrack(0, d)
    # return possible

if __name__ == "__main__":
    # start = timer()
    # available, desired = parse_input("puzzle_input/d19_input.txt")
    # result = solution_1(available, desired)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution1: {result}')

    start = timer()
    available, desired = parse_input("puzzle_input/d19_input.txt")
    result = solution_2(available, desired)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')

