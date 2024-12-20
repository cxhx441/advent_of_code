from timeit import default_timer as timer
import collections

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        racetrack = []
        for line in f:
            row = [ch for ch in line.strip()]
            racetrack.append(row)
    return racetrack

def get_start(racetrack):
    ROWS, COLS = len(racetrack), len(racetrack[0])
    for r in range(ROWS):
        for c in range(COLS):
            if racetrack[r][c] == 'S':
                return r, c

def best_wo_cheats(racetrack):
    start = get_start(racetrack)
    q = collections.deque([(*start, 0, [])])
    seen = set()
    while q:
        r, c, ps, path = q.popleft()
        if racetrack[r][c] == '#' or (r, c) in seen:
            continue

        seen.add((r, c))
        if racetrack[r][c] == 'E':
            return ps, path[:-1]
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            q.append( (nr, nc, ps + 1, path + [(nr, nc)]) )

def best_w_cheats(racetrack):
    start = get_start(racetrack)
    q = collections.deque([(*start, 0, False)])
    seen = set()
    while q:
        r, c, ps = q.popleft()
        if racetrack[r][c] == '#' or (r, c) in seen:
            continue

        seen.add((r, c))
        if racetrack[r][c] == 'E':
            return ps
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            q.append( (nr, nc, ps + 1) )


def solution_1(racetrack):
    stnd = best_wo_cheats(racetrack)
    return stnd
    # savings = find_best_with_cheats(racetrack, start, stnd)


def solution_2(racetrack):
    pass

if __name__ == "__main__":
    start = timer()
    racetrack = parse_input("puzzle_input/d20_input.txt")
    result = solution_1(racetrack)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')

    # start = timer()
    # available, desired = parse_input("puzzle_input/d20_input.txt")
    # result = solution_2(available, desired)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution1: {result}')

