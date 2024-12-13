from timeit import default_timer as timer
import collections

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        grid = []
        for line in f:
            grid.append([ x for x in line[:-1] ] )
    return grid

def solution_1(grid):
    def dfs(r, c):
        CHAR = grid[r][c]
        q = collections.deque([(r, c)])
        this_seen = set()
        perimeter = 0
        area = 0
        while q:
            r, c = q.popleft()
            if r not in range(ROWS) or c not in range(COLS):
                perimeter += 1
                continue

            if (r, c) in this_seen:
                continue

            if grid[r][c] != CHAR:
                perimeter += 1
                continue

            grid[r][c] = '#'
            this_seen.add((r, c))
            area += 1
            q.append((r + 1, c))
            q.append((r - 1, c))
            q.append((r, c + 1))
            q.append((r, c - 1))

        cost = perimeter * area
        return cost

    ROWS, COLS = len(grid), len(grid[0])
    total = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != '#':
                total += dfs(r, c)
    return total


def solution_2(grid):
    def condense(fences, perimeter):
        seen = set()
        these_fences = 0
        for r, c, dir in fences:
            if (r, c, dir) in seen:
                continue

            these_fences += 1
            i = 0
            while (r + i, c, dir) in fences:
                seen.add((r + i, c, dir))
                i += 1

            i = 0
            while (r - i, c, dir) in fences:
                seen.add((r - i, c, dir))
                i += 1

            j = 0
            while (r, c + j, dir) in fences:
                seen.add((r, c + j, dir))
                j += 1

            j = 0
            while (r, c - j, dir) in fences:
                seen.add((r, c - j, dir))
                j += 1

        return these_fences

    def dfs(r, c):
        CHAR = grid[r][c]
        q = collections.deque([(r, c, None)])
        this_seen = set()
        perimeter = 0
        fences = set()
        area = 0
        while q:
            r, c, dir = q.popleft()
            if r not in range(ROWS) or c not in range(COLS):
                perimeter += 1
                fences.add((r, c, dir))
                continue

            if (r, c) in this_seen:
                continue

            if grid[r][c] != CHAR:
                perimeter += 1
                fences.add((r, c, dir))
                continue

            grid[r][c] = '#'
            this_seen.add((r, c))
            area += 1
            q.append((r, c + 1, 'v1'))
            q.append((r + 1, c, 'h1'))
            q.append((r, c - 1, 'v2'))
            q.append((r - 1, c, 'h2'))

        fence_special = condense(fences, perimeter)
        cost = fence_special * area
        return cost

    ROWS, COLS = len(grid), len(grid[0])
    total = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != '#':
                total += dfs(r, c)
    return total

if __name__ == '__main__':
    start = timer()
    grid = parse_input("puzzle_input//d12_input.txt")
    result = solution_1(grid)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')


    start = timer()
    grid = parse_input("puzzle_input//d12_input.txt")
    result = solution_2(grid)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution2: {result}')
