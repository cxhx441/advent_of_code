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
    dp = [ [float("inf")] * COLS for _ in range(ROWS) ]
    total = 0
    direction = 'E'
    h = [(total, position[0], position[1], direction)]
    while h:
        cur_tot, r, c, cur_dir = heapq.heappop(h)
        if not ( 0 <= r < ROWS and 0 <= c < COLS ) or maze[r][c] == '#':
            continue

        if cur_tot >= dp[r][c]:
            continue

        dp[r][c] = cur_tot
        for dir in directions:
            nr, nc = r + directions[dir][0], c + directions[dir][1]
            if dir == cur_dir:
                heapq.heappush(h, (cur_tot + 1, nr, nc, dir) )
            else:
                heapq.heappush(h, (cur_tot + 1001, nr, nc, dir) )

    end = get_position(maze, 'E')

    return dp[end[0]][end[1]]


def solution_2(maze):
    ROWS, COLS = len(maze), len(maze[0])
    start = get_position(maze, 'S')
    dp = [ [float("inf")] * COLS for _ in range(ROWS) ]
    total = 0
    direction = 'E'
    best = float("inf")
    best_seats = []
    h = [(total, start[0], start[1], direction, [start])]
    while h:
        cur_tot, r, c, cur_dir, path = heapq.heappop(h)
        if not ( 0 <= r < ROWS and 0 <= c < COLS ) or maze[r][c] == '#':
            continue

        if cur_tot > best:
            continue
        dp[r][c] = cur_tot

        if cur_tot <= best  and maze[r][c] == 'E':
            best = cur_tot
            best_seats += path

        for dir in directions:
            nr, nc = r + directions[dir][0], c + directions[dir][1]
            if dir == cur_dir:
                heapq.heappush(h, (cur_tot + 1, nr, nc, dir, path + [(nr, nc)]) )
            else:
                heapq.heappush(h, (cur_tot + 1001, nr, nc, dir, path + [(nr, nc)]) )

    # print(tabulate(dp))
    print(best, len(set(best_seats)))
    return len(set(best_seats))

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
    result_2 = solution_2(maze, solution_1(maze))
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution2: {result_2}')
