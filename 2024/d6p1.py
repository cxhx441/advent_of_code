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
        location = None
        direction = None
        grid = []
        r = 0
        for line in f:
            row = []
            for c, ch in enumerate(line[:-1]):
                if ch in dirs:
                    location = (r, c)
                    direction = ch
                row.append(ch)
            grid.append( row )
            r += 1
    return grid, location, direction

def solution(grid, location, direction):
    r, c = location
    ROWS, COLS = len(grid), len(grid[0])
    seen = set(())

    # while r in range(0, ROWS) and c in range(0, COLS):
    while r + dirs[direction][0] in range(ROWS) and c + dirs[direction][1] in range(COLS):
        grid[r][c] = 'X'
        while grid[r + dirs[direction][0]][c + dirs[direction][1]] == '#':
            if direction == '^': direction = '>'
            elif direction == '>': direction = 'v'
            elif direction == 'v': direction = '<'
            elif direction == '<': direction = '^'

        r, c = r + dirs[direction][0], c + dirs[direction][1]
        seen.add((r, c))

    return len(seen)


filename = "2024//d6p1_input_ex.txt"
grid, location, direction = read_input(filename)
result = solution(grid, location, direction)
print(result)
assert result == 41

start = timer()
filename = "2024//d6p1_input.txt"
rules, inverse_rules, updates = read_input(filename)
result = solution(rules, inverse_rules, updates)
print(result)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result)
