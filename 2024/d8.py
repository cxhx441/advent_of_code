from timeit import default_timer as timer
import collections

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        grid = []
        for line in f:
            grid.append( [ x for x in line[:-1]] )
    return grid

def solution_1(grid):
    ROWS, COLS = len(grid), len(grid[0])
    def get_antennas(grid):
        antennas = collections.defaultdict(list)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != '.':
                    frequency = grid[r][c]
                    antennas[frequency].append((r, c))
        return antennas

    def get_antinodes(l1, l2):
        vector = l2[0] - l1[0], l2[1] - l1[1]
        # vector21 = l1[0] - l2[0], l1[1] - l2[1]
        antinode12 = l2[0] + vector[0], l2[1] + vector[1]
        antinode21 = l1[0] - vector[0], l1[1] - vector[1]

        antinodes = set()
        if antinode12[0] in range(ROWS) and antinode12[1] in range(COLS):
            antinodes.add(antinode12)
        if antinode21[0] in range(ROWS) and antinode21[1] in range(COLS):
            antinodes.add(antinode21)
        return antinodes

    antennas = get_antennas(grid)
    antinodes = set()
    for locations in antennas.values():
        for i, l1 in enumerate(locations):
            for l2 in locations[i + 1:]:
                new_antinodes = get_antinodes(l1, l2)
                antinodes = antinodes.union(new_antinodes)

    return len(antinodes)

grid = parse_input("2024//puzzle_input//d8_input_ex1.txt")
result_1 = solution_1(grid)
print(result_1)
assert result_1 == 14

start = timer()
input = parse_input("2024//puzzle_input//d8_input.txt")
result = solution_1(input)
print(result)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result)


def solution_2(x):
    ROWS, COLS = len(grid), len(grid[0])
    def get_antennas(grid):
        antennas = collections.defaultdict(list)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != '.':
                    frequency = grid[r][c]
                    antennas[frequency].append((r, c))
        return antennas

    def get_antinodes(l1, l2):
        vector = l2[0] - l1[0], l2[1] - l1[1]

        antinodes = set()
        r, c = l1
        while r in range(ROWS) and c in range(COLS):
            antinodes.add((r, c))
            r += vector[0]
            c += vector[1]

        r, c = l2
        while r in range(ROWS) and c in range(COLS):
            antinodes.add((r, c))
            r -= vector[0]
            c -= vector[1]

        return antinodes

    antennas = get_antennas(grid)
    antinodes = set()
    for locations in antennas.values():
        for i, l1 in enumerate(locations):
            for l2 in locations[i + 1:]:
                new_antinodes = get_antinodes(l1, l2)
                antinodes = antinodes.union(new_antinodes)

    return len(antinodes)

grid = parse_input("2024//puzzle_input//d8_input_ex1.txt")
result_2 = solution_2(grid)
print(result_2)
assert result_2 == 34

grid = parse_input("2024//puzzle_input//d8_input_ex2.txt")
result_2 = solution_2(grid)
print(result_2)
assert result_2 == 9

start = timer()
grid = parse_input("2024//puzzle_input//d8_input.txt")
result_2 = solution_2(grid)
print(result_2)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result_2)
