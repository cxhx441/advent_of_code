from timeit import default_timer as timer

# def parse_input(filename):
#     with open(filename, 'r', encoding="UTF-8") as f:

def solution_1(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        locks_n_keys = f.read().split('\n\n')

    locks = []
    keys = []
    for lnk in locks_n_keys:
        lnk = lnk.strip('\n')
        lnk = lnk.split('\n')
        col_counts = [0] * 5
        if lnk[0] == '#' * 5 and lnk[6] == '.' * 5: # lock
            for row in lnk[1:]:
                for c in range(len(row)):
                    if row[c] == '#':
                        col_counts[c] += 1
            locks.append(col_counts)
        elif lnk[0] == '.' * 5 and lnk[6] == '#' * 5: # key
            for row in lnk[:-1]:
                for c in range(len(row)):
                    if row[c] == '#':
                        col_counts[c] += 1
            keys.append(col_counts)

    unlocked = 0
    for key in keys:
        for lock in locks:
            matched = [ ki + li for ki, li in zip(key, lock) if ki + li > 5]
            if matched == []:
                unlocked += 1

    return unlocked


def solution_2(filename):
    return 0


if __name__ == "__main__":
    start = timer()
    unlocked = solution_1("puzzle_input/d25_input.txt")
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {unlocked}')

    # print()
    # start = timer()
    # edges = parse_input("puzzle_input/d23_input.txt")
    # best = solution_2(edges)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution2: {best}')
    #
