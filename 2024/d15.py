from timeit import default_timer as timer
import collections

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


def get_start(grid):
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '@':
                return (r, c)


move_dic = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}

def solution_1(grid, moves):
    def get_cost(grid):
        ROWS, COLS = len(grid), len(grid[0])
        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 'O':
                    total += 100 * r + c
        return total

    r, c = get_start(grid)
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


def upsize_grid(grid):
    upsized_grid = []
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        row = []
        for c in range(COLS):
           """  If the tile is #, the new map contains ## instead. 
                If the tile is O, the new map contains [] instead.
                If the tile is ., the new map contains .. instead.
                If the tile is @, the new map contains @. instead.
           """
           if grid[r][c] == '#':
               row.extend(['#', '#'])
           elif grid[r][c] == 'O':
               row.extend(['[', ']'])
           elif grid[r][c] == '.':
               row.extend(['.', '.'])
           elif grid[r][c] == '@':
               row.extend(['@', '.'])
        upsized_grid.append(row)
    return upsized_grid

def solution_2(grid, moves):
    def get_cost(grid):
        ROWS, COLS = len(grid), len(grid[0])
        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '[':
                    total += 100 * r + c
        return total

    def push_h(move, start):
        dc = move_dic[move][1]

        r, c = start
        while grid[r][c] != '.' and grid[r][c] != '#':
            c += dc

        if grid[r][c] == '#':
            return start

        r, c = start
        prev = '.'
        while grid[r][c] != '.':
            cur = grid[r][c]
            grid[r][c] = prev
            prev = cur
            c += dc
        grid[r][c] = prev
        return start[0], start[1] + dc

    def push_v(move, start):
        dr = move_dic[move][0]

        # q = collections.deque([start])
        q = set()
        q.add( (start[0], start[1]) )
        while q:
            new_q = set()
            lq = len(q)
            for _ in range(lq):
                r, c = q.pop()
                if grid[r][c] != '.' and grid[r][c] != '#':
                    r += dr
                    if grid[r][c] == '[':
                        new_q.add((r, c))
                        new_q.add((r, c + 1))
                    elif grid[r][c] == ']':
                        new_q.add((r, c))
                        new_q.add((r, c - 1))
                    elif grid[r][c] == '#':
                        return start
            q = new_q

        q = set()
        q.add( (start[0], start[1], '.') )
        while q:
            new_q = set()
            lq = len(q)
            for _ in range(lq):
                r, c, prev = q.pop()
                cur = grid[r][c]
                grid[r][c] = prev

                if cur != '.':
                    r += dr
                    if grid[r][c] == '[':
                        new_q.add((r, c, cur))
                        if cur == '[':
                            new_q.add((r, c + 1, ']'))
                        else:
                            new_q.add((r, c + 1, '.'))
                    elif grid[r][c] == ']':
                        new_q.add((r, c, cur))
                        if cur == ']':
                            new_q.add((r, c - 1, '['))
                        else:
                            new_q.add((r, c - 1, '.'))
                    elif grid[r][c] == '.':
                        new_q.add((r, c, cur))

            q = new_q
        return start[0] + dr, start[1]

    print_grid(grid)
    print()
    start = get_start(grid)
    mv_i = 0
    for move in moves:
        if is_error(grid):
            break
        if move == '<' or move == '>':
            start = push_h(move, start)
        elif move == 'v' or move == '^':
            start = push_v(move, start)
        # print(move)
        # print_grid(grid)
        # if mv_i + 1 < len(moves):
        #     print(moves[mv_i + 1])
        #     mv_i += 1
        # print()


    print_grid(grid)
    cost = get_cost(grid)
    return cost

def is_error(grid):
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '[':
                if grid[r][c + 1] != ']':
                    return True
            elif grid[r][c] == ']':
                if grid[r][c - 1] != '[':
                    return True
    return False


# 1444879 too high
# 1422938 too low
if __name__ == "__main__":
    pass
    start = timer()
    grid, moves = parse_input("puzzle_input//d15_input.txt")
    result = solution_1(grid, moves)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')


    start = timer()
    grid, moves = parse_input("puzzle_input//d15_input.txt")
    upsized_grid = upsize_grid(grid)
    result_2 = solution_2(upsized_grid, moves)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution2: {result_2}')
