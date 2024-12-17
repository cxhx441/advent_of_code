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

        q = set()
        q.add( (start[0], start[1]) )
        # q = collections.deque()
        # q.append( (start[0], start[1]) )
        while q:
            # new_q = collections.deque()
            new_q = set()
            lq = len(q)
            for _ in range(lq):
                # r, c = q.popleft()
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
        all = set()
        q.add( (start[0], start[1], '@') )
        while q:
            all = all.union(q)
            # new_q = collections.deque()
            new_q = set()
            lq = len(q)
            for _ in range(lq):
                r, c, bracket = q.pop()
                if grid[r][c] != '.' and grid[r][c] != '#':
                    r += dr
                    if grid[r][c] == '[':
                        new_q.add((r, c, '['))
                        new_q.add((r, c + 1, ']'))
                    elif grid[r][c] == ']':
                        new_q.add((r, c - 1, '['))
                        new_q.add((r, c, ']'))
            q = new_q

        for r, c, bracket in all:
            grid[r][c] = '.'
        for r, c, bracket in all:
            grid[r + dr][c] = bracket

        # r, c = start
        # grid[r][c] = '.'
        # nr = r + dr
        # q = collections.deque()
        # if grid[nr][c] == '[':
        #     grid[r][c] = '@'
        #     grid[r][c+1] = '.'
        #     q.append((nr, c, '['))
        #     q.append((nr, c + 1, ']'))
        # elif grid[nr][c] == ']':
        #     grid[r][c-1] = '.'
        #     grid[r][c] = '@'
        #     q.append((nr, c - 1, '['))
        #     q.append((nr, c, ']'))
        #
        # while q:
        #     lq = len(q)
        #     if lq == 2:
        #         r, c0, prev0 = q.popleft()
        #         r, c1, prev1 = q.popleft()
        #
        #         cur0 = grid[r][c0]
        #         cur1 = grid[r][c1]
        #         grid[r][c0] = prev0
        #         grid[r][c1] = prev1
        #
        #         prev0 = cur0
        #         prev1 = cur1
        #
        #         nr = r + dr
        #         if grid[nr][c0] == '[' and grid[nr][c1] == ']':
        #             q.append((nr, c0, '['))
        #             q.append((nr, c1, ']'))
        #         elif grid[nr][c0] == ']' and grid[nr][c1] == '[':
        #             q.append((nr, c0, '['))
        #             q.append((nr, c1, ']'))
        #
        #

        return start[0] + dr, start[1]

    print_grid(grid)
    print()
    start = get_start(grid)
    for i, move in enumerate(moves):
        # if i >= 14086:
        #     print_grid(grid)
        # if is_error(grid):
        #     print(f'error at: {i}')
        #     return None
        if move == '<' or move == '>':
            start = push_h(move, start)
        elif move == 'v' or move == '^':
            start = push_v(move, start)
        # print(move)
        # print_grid(grid)
        # if i + 1 < len(moves):
        #     print(moves[i + 1])
        #     i += 1
        # print()


    # print_grid(grid)
    cost = get_cost(grid)
    return cost

def is_error(grid):
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '[':
                if grid[r][c + 1] != ']':
                    print_grid(grid)
                    return True
            elif grid[r][c] == ']':
                if grid[r][c - 1] != '[':
                    print_grid(grid)
                    return True
    return False

# 1506177 too high
# 1444879 too high
# 1435773
# 1426660
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
