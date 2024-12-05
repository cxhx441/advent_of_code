from timeit import default_timer as timer

def read_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        grid = []
        for line in f:
            grid.append([c for c in line[:-1]])
    return grid

def solution(grid):
    def diag(r, c):
        return { 'M', 'S' } == { grid[r - 1][c + 1], grid[r + 1][c - 1] }

    def antidiag(r, c):
        return { 'M', 'S' } == { grid[r - 1][c - 1], grid[r + 1][c + 1] }

    count = 0
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(1, ROWS - 1):
        for c in range(1, COLS - 1):
            if grid[r][c] == 'A':
                if diag(r, c) and antidiag(r, c):
                    count += 1

    print(count)
    return count

filename = "2024//d4p1_input_ex.txt"
grid = read_input(filename)
assert solution(grid) == 9

start = timer()
filename = "2024//d4p1_input.txt"
grid = read_input(filename)
result = solution(grid)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result)
