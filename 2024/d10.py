from timeit import default_timer as timer

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        grid = []
        for line in f:
            grid.append( [ int(num) for num in line[:-1] ] )
    return grid

def get_starts(grid):
    starts = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                starts.append( (r, c) )
    return starts

def dfs_w_seen(start, grid):
    stack = [start]
    seen = set()
    ROWS, COLS = len(grid), len(grid[0])
    nine_count = 0
    while stack:
        r, c = stack.pop()
        if (r, c) in seen:
            continue
        seen.add((r, c))

        if grid[r][c] == 9:
            nine_count += 1
            continue
        if r + 1 in range(ROWS) and grid[r][c] + 1 == grid[r + 1][c]:
            stack.append((r + 1, c))
        if c + 1 in range(COLS) and grid[r][c] + 1 == grid[r][c + 1]:
            stack.append((r, c + 1))
        if r - 1 in range(ROWS) and grid[r][c] + 1 == grid[r - 1][c]:
            stack.append((r - 1, c))
        if c - 1 in range(COLS) and grid[r][c] + 1 == grid[r][c - 1]:
            stack.append((r, c - 1))
    return nine_count

def dfs_wo_seen(start, grid):
    stack = [start]
    ROWS, COLS = len(grid), len(grid[0])
    nine_count = 0
    while stack:
        r, c = stack.pop()

        if grid[r][c] == 9:
            nine_count += 1
            continue

        if r + 1 in range(ROWS) and grid[r][c] + 1 == grid[r + 1][c]:
            stack.append((r + 1, c))
        if c + 1 in range(COLS) and grid[r][c] + 1 == grid[r][c + 1]:
            stack.append((r, c + 1))
        if r - 1 in range(ROWS) and grid[r][c] + 1 == grid[r - 1][c]:
            stack.append((r - 1, c))
        if c - 1 in range(COLS) and grid[r][c] + 1 == grid[r][c - 1]:
            stack.append((r, c - 1))
    return nine_count



def solution_1(grid):
    starts = get_starts(grid)
    nine_counts = 0
    for s in starts:
        nine_counts += dfs_w_seen(s, grid)
    return nine_counts

def solution_2(grid):
    starts = get_starts(grid)
    nine_counts = 0
    for s in starts:
        nine_counts += dfs_wo_seen(s, grid)
    return nine_counts

if __name__ == '__main__':
    start = timer()
    input = parse_input("puzzle_input//d10_input.txt")
    result_1 = solution_1(input)
    end = timer()
    print( f"{round( ( end - start ) * 1000, 2 )}ms" )
    print(f'Solution 1: {result_1}')

    start = timer()
    input = parse_input("puzzle_input//d10_input.txt")
    result_2 = solution_2(input)
    end = timer()
    print( f"{round( ( end - start ) * 1000, 2 )}ms" )
    print(f'Solution 2: {result_2}')
