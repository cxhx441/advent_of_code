from timeit import default_timer as timer
import collections
import heapq
import re

def parse_input(filename, n):
    with open(filename, 'r', encoding="UTF-8") as f:
        data = f.read().strip()
        pattern = r"(\d+),(\d+)"
        matches = re.findall(pattern, data)
        bytes = [ (int(r), int(c)) for c, r in matches ]

    grid = [ ['.'] * (n+1) for _ in range(n+1) ]
    return grid, bytes

def drop(grid, bytes, count):
    for i in range(count):
        r, c = bytes[i]
        grid[r][c] = '#'

def solution_1(grid, bytes, count):
    ROWS, COLS = len(grid), len(grid[0])
    drop(grid, bytes, count)
    start = (0, 0)
    # q = collections.deque([*start, 0])
    # seen = set()
    # while q:
    #     r, c, steps = q.popleft()
    #     if (r, c) in seen:
    #         continue
    #     seen.add((r, c))
    #     dp[r][c] = steps

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
    return dp[-1][-1]


def dijkstra(grid):
    ROWS, COLS = len(grid), len(grid[0])
    start = (0, 0)
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
    return dp[-1][-1]

def solution_2(grid, bytes):
    for i in range(len(bytes)):
        print(i)
        byte = bytes[i]
        r, c = byte
        grid[r][c] = '#'
        if dijkstra(grid) == float("inf"):
            return bytes[i][::-1]
    return None

if __name__ == "__main__":
    start = timer()
    grid, bytes = parse_input("puzzle_input//d18_input.txt", 70)
    result = solution_1(grid, bytes, 1024)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')

    start = timer()
    grid, bytes = parse_input("puzzle_input//d18_input.txt", 70)
    result = solution_2(grid, bytes)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')

