from timeit import default_timer as timer
import collections
import heapq
from tabulate import tabulate

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        maze = []
        for line in f:
            # row = [ ch for ch in line[:-1]]
            maze.append(line[:-1])
    return maze


def get_position(grid, target):
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == target:
                return (r, c)

directions = {
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
    'N': (-1, 0),
}
def solution_1(maze):
    ROWS, COLS = len(maze), len(maze[0])

    position = get_position(maze, 'S')
    dp = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            row.append(
                {
                    'E': float("inf"),
                    'S': float("inf"),
                    'W': float("inf"),
                    'N': float("inf")
                 }
            )
        dp.append(row)
    total = 0
    direction = 'E'
    h = [(total, *position, direction)]
    while h:
        cur_tot, r, c, d = heapq.heappop(h)
        if not ( 0 <= r < ROWS and 0 <= c < COLS ) or maze[r][c] == '#':
            continue

        if cur_tot >= dp[r][c][d]:
            continue

        dp[r][c][d] = cur_tot
        for dir in directions:
            nr, nc = r + directions[dir][0], c + directions[dir][1]
            if dir == d:
                heapq.heappush(h, (cur_tot + 1, nr, nc, dir) )
            else:
                heapq.heappush(h, (cur_tot + 1001, nr, nc, dir) )

    end = get_position(maze, 'E')

    return min(dp[end[0]][end[1]].values())


def solution_2(maze):
    ROWS, COLS = len(maze), len(maze[0])
    start = get_position(maze, 'S')
    dp = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            row.append(
                {
                    'E': [ float("inf"), set() ],
                    'S': [ float("inf"), set() ],
                    'W': [ float("inf"), set() ],
                    'N': [ float("inf"), set() ],
                }
            )
        dp.append(row)
    total = 0
    direction = 'E'
    h = [ ( total, *start, direction, {start} ) ]
    best_seats = set()
    best_time = float("inf")
    while h:
        cur_tot, r, c, d, path = heapq.heappop(h)
        if not ( 0 <= r < ROWS and 0 <= c < COLS ) or maze[r][c] == '#':
            continue

        if maze[r][c] == 'E' and cur_tot <= best_time:
            if cur_tot < best_time:
                best_time = cur_tot
                best_seats = path.copy()
            elif cur_tot == best_time:
                best_seats = best_seats.union(path)

        if cur_tot > dp[r][c][d][0]:
            continue

        dp[r][c][d][1].add((r, c))
        dp[r][c][d][0] = cur_tot
        for dir in directions:
            nr, nc = r + directions[dir][0], c + directions[dir][1]
            if dir == d:
                heapq.heappush(h, (cur_tot + 1, nr, nc, dir, path.union( {(nr, nc)} ) ) )
            else:
                heapq.heappush(h, (cur_tot + 1001, nr, nc, dir, path.union( {(nr, nc)} ) ) )

    end = get_position(maze, 'E')

    # return min(dp[end[0]][end[1]].values())
    # return best_time, best_seats, len(best_seats)
    return len(best_seats)

if __name__ == "__main__":
    pass
    start = timer()
    maze = parse_input("puzzle_input//d16_input.txt")
    result = solution_1(maze)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')


    start = timer()
    maze = parse_input("puzzle_input//d16_input.txt")
    result_2 = solution_2(maze)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution2: {result_2}')
