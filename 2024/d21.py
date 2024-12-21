from timeit import default_timer as timer
import collections
import heapq
from tabulate import tabulate

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

def get_end(racetrack):
    ROWS, COLS = len(racetrack), len(racetrack[0])
    for r in range(ROWS):
        for c in range(COLS):
            if racetrack[r][c] == 'E':
                return r, c

def best_wo_cheats(racetrack):
    start = get_start(racetrack)
    q = collections.deque([(*start, 0, [start])])
    seen = set()
    while q:
        r, c, ps, path = q.popleft()
        if racetrack[r][c] == '#' or (r, c) in seen:
            continue

        seen.add((r, c))
        if racetrack[r][c] == 'E':
            return ps, path
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            q.append( (nr, nc, ps + 1, path + [(nr, nc)] ) )

def best_w_cheats(racetrack):
    pass


def solution_1(racetrack, minimum_saving):
    stnd = best_wo_cheats(racetrack)
    ROWS, COLS = len(racetrack), len(racetrack[0])
    counts = collections.defaultdict(lambda: 0)
    for r in range(1, ROWS-1):
        print(r)
        for c in range(1, COLS-1):
            if racetrack[r][c] == '#':
                racetrack[r][c] = '.'
                savings = stnd - best_wo_cheats(racetrack)
                if savings >= minimum_saving:
                    counts[savings] += 1
                racetrack[r][c] = '#'

    return sum(counts.values())
    # savings = find_best_with_cheats(racetrack, start, stnd)

def dijkstra(grid, start):
    ROWS, COLS = len(grid), len(grid[0])
    dp = [ [float("inf")] * COLS for _ in range(ROWS) ]
    h = [(0, *start)]
    while h:
        cost, r, c = heapq.heappop(h)
        if cost >= dp[r][c] or grid[r][c] == '#':
            continue
        dp[r][c] = cost
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                continue
            heapq.heappush(h, (cost + 1, nr, nc))
    return dp

def get_radius_nodes(start, racetrack, radius):
    deltas = set()
    q = collections.deque([start])
    for _ in range(radius):
        r, c = q.popleft()
        if (r, c) in deltas:
            continue
        deltas.add((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            q.append((nr, nc))
    return deltas

# def filter_deltas(racetrack, deltas, start):
#     ROWS, COLS = len(racetrack), len(racetrack[0])
#     filtered_deltas = set()
#     for (r, c) in deltas:
#         if not (0 <= r < ROWS and 0 <= c < COLS):
#             continue



def solution_2(racetrack, minimum_saving):
    ROWS, COLS = len(racetrack), len(racetrack[0])
    stnd, path = best_wo_cheats(racetrack)
    end = get_end(racetrack)
    dij_dp = dijkstra(racetrack, end)
    # print(tabulate(dij_dp))

    valid_cheats = collections.defaultdict(lambda: 0)
    for standard_time, (r, c) in enumerate(path):

        cheat_time = 0
        q = collections.deque([(r, c, cheat_time)])
        seen = set()
        while q:
            r, c, cheat_time = q.popleft()
            if not ( 0 <= r < ROWS and 0 <= c < COLS ):
                continue

            if (r, c) in seen or cheat_time > 20:
                continue
            seen.add((r, c))

            if dij_dp[r][c] < float("inf"):
                path_time = standard_time + dij_dp[r][c]
                faster = cheat_time + path_time
                saved = stnd - faster
                if saved >= minimum_saving:
                    valid_cheats[saved] += 1

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                q.append((nr, nc, cheat_time + 1))
    return sum(valid_cheats.values())


if __name__ == "__main__":
    # start = timer()
    # racetrack = parse_input("puzzle_input/d20_input.txt")
    # result = solution_1(racetrack, 100)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution1: {result}')

    start = timer()
    # racetrack = parse_input("puzzle_input/d20_input_ex1.txt")
    # result = solution_2(racetrack, 50)
    racetrack = parse_input("puzzle_input/d20_input.txt")
    result = solution_2(racetrack, 100)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')

