from timeit import default_timer as timer

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        data = f.read()
        data_grid, data_moves = data.split('\n\n')
        data_grid = data_grid.split('\n')
        data_moves = data_moves.split('\n')
        grid = []
        for dg in data_grid:
            grid.append([ c for c in dg ])
        moves = ''.join(data_moves)
    return grid, moves

def print_grid(grid):
    grid_strs = []
    for r in range(len(grid)):
        grid_strs.append(''.join(grid[r]))
    print('\n'.join(grid_strs))


def solution_1(grid, moves):
    def get_start():
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '@':
                    return (r, c)
    def get_cost(grid):
        ROWS, COLS = len(grid), len(grid[0])
        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 'O':
                    total += 100 * r + c
        return total


    move_dic = { '>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0) }

    r, c = get_start()
    for move in moves:
        dr, dc = move_dic[move]
        tr, tc = r + dr, c + dc
        stack = [(r, c)]
        while grid[tr][tc] != '#' and grid[tr][tc] != '.':
            stack.append( (tr, tc) )
            tr, tc = tr + dr, tc + dc

        if grid[tr][tc] == '#':
            # print(move)
            # print_grid(grid)
            # print()
            continue
        elif grid[tr][tc] == '.':
            while stack:
                nr, nc = stack.pop()
                grid[tr][tc] = grid[nr][nc]
                tr, tc = nr, nc
            grid[r][c] = '.'
            r, c = r + dr, c + dc
        # print(move)
        # print_grid(grid)
        # print()

    cost = get_cost(grid)
    return cost


def solution_2(x):
    return 0

if __name__ == "__main__":
    pass
    start = timer()
    grid, moves = parse_input("puzzle_input//d15_input.txt")
    result = solution_1(grid, moves)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')


    # start = timer()
    # grid, moves = parse_input("puzzle_input//d15_input.txt")
    # result_2 = solution_2(grid, moves)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution2: {result_2}')
