from timeit import default_timer as timer

def read_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        grid = []
        for line in f:
            grid.append([c for c in line[:-1]])
    return grid

def solution(grid):
    count = 0
    target = [ c for c in 'XMAS']

    def trek(i, r, c, dr, dc):
        nonlocal count
        if i == len(target):
            count += 1
            return

        if r < 0 or r >= ROWS or\
           c < 0 or c >= COLS or\
           grid[r][c] != target[i]:
            return

        if grid[r][c] != target[i]:
            return

        trek(i + 1, r + dr, c + dc, dr, dc)

    neighbors = [ (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1) ]
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            for (dr, dc) in neighbors:
                trek(0, r, c, dr, dc)

    print(count)
    return count

filename = "2024//d4p1_input_ex.txt"
grid = read_input(filename)
assert solution(grid) == 18

start = timer()
filename = "2024//d4p1_input.txt"
grid = read_input(filename)
result = solution(grid)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result)
