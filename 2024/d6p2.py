from timeit import default_timer as timer
import collections

dirs = {
    '^' : (-1, 0),
    '>' : (0, 1),
    'v' : (1, 0),
    '<' : (0, -1)
    }

def read_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        start = None
        direction = None
        grid = []
        r = 0
        for line in f:
            row = []
            for c, ch in enumerate(line[:-1]):
                if ch in dirs:
                    start = (r, c)
                    direction = ch
                row.append(ch)
            grid.append( row )
            r += 1
    return grid, start, direction

def traverse(grid, start, direction):
    r, c = start
    start = ((direction, r, c))
    ROWS, COLS = len(grid), len(grid[0])
    seen = set()
    # while r in range(0, ROWS) and c in range(0, COLS):
    while r + dirs[direction][0] in range(ROWS) and c + dirs[direction][1] in range(COLS):
        grid[r][c] = 'X'
        while grid[r + dirs[direction][0]][c + dirs[direction][1]] == '#':
            if direction == '^': direction = '>'
            elif direction == '>': direction = 'v'
            elif direction == 'v': direction = '<'
            elif direction == '<': direction = '^'

        r, c = r + dirs[direction][0], c + dirs[direction][1]
        if (direction, r, c) in seen:
            return True
        seen.add((direction, r, c))

    return False

def get_touched(grid, start, direction):
    r, c = start
    start = ((direction, r, c))
    ROWS, COLS = len(grid), len(grid[0])
    seen = set()
    while r + dirs[direction][0] in range(ROWS) and c + dirs[direction][1] in range(COLS):
        grid[r][c] = 'X'
        while grid[r + dirs[direction][0]][c + dirs[direction][1]] == '#':
            if direction == '^': direction = '>'
            elif direction == '>': direction = 'v'
            elif direction == 'v': direction = '<'
            elif direction == '<': direction = '^'

        r, c = r + dirs[direction][0], c + dirs[direction][1]
        seen.add((r, c))

    return seen

# 41.5 seconds original
# 1688
def solution(grid, start, direction, touched):
    ROWS, COLS = len(grid), len(grid[0])
    valid = 0
    for r in range(ROWS):
        for c in range(COLS):
            # print((r, c))
            if (r, c) not in touched or grid[r][c] == '#' or (r, c) == start:
                continue

            grid[r][c] = '#'
            if traverse(grid, start, direction):
                valid += 1
            grid[r][c] = '.'
    return valid


filename = "2024//d6p1_input_ex.txt"
grid, start, direction = read_input(filename)
touched = get_touched(grid, start, direction)
result = solution(grid, start, direction, touched)
print(result)
assert result == 6

t0 = timer()
filename = "2024//d6p1_input.txt"
grid, start, direction = read_input(filename)
touched = get_touched(grid, start, direction)
result = solution(grid, start, direction, touched)
print(result)
t1 = timer()
print( f"{( t1 - t0 ) * 1000}ms" )
print(result)
