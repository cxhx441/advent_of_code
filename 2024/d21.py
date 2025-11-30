from timeit import default_timer as timer

import networkx
import networkx as nx
import collections
from functools import cache

KEYPAD = [['7', '8', '9'],
          ['4', '5', '6'],
          ['1', '2', '3'],
          [' ', '0', 'A']]

DPAD =   [[' ', '^', 'A'],
          ['<', 'v', '>'] ]


def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        codes = []
        for line in f:
            codes.append(line.strip())
    return codes

# i could run dijkstra on each node in each pad to find the best paths, but i'll try networkx
keypad_paths = []
dpad_paths = []
def get_paths(pad):
    G = networkx.DiGraph()
    ROWS, COLS = len(pad), len(pad[0])
    for r in range(ROWS):
        for c in range(COLS):
            key = pad[r][c]
            if key == ' ':
                continue
            G.add_node(key, pos=(r, c))
            for dr, dc, direction in [ (0, 1, '>'), (1, 0, 'v'), (0, -1, '<'), (-1, 0, '^') ]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < ROWS and 0 <= nc < COLS) or pad[nr][nc] == ' ':
                    continue
                G.add_edge(key, pad[nr][nc], direction=direction)

    paths = collections.defaultdict(list)
    for n0 in G.nodes():
        for n1 in G.nodes():
            if n0 == n1:
                continue

            cur_paths = list(nx.all_shortest_paths(G, n0, n1))
            for path in cur_paths:
                directions = [ (G[path[i]][path[i + 1]]['direction']) for i in range( len(path) - 1 ) ]
                paths[(n0, n1)].append( ''.join(directions) )

    return paths

@cache
def get_length(lvl, txt):
    if lvl == NUM_BOTS + 1: # that'd be the human
        return len(txt)

    paths = k_paths if lvl == 0 else d_paths
    keystroke_total = 0
    for n0, n1 in zip('A' + txt, txt): # genius. A029A, 029A
        min_keystrokes = []
        for path in paths[(n0, n1)]:
            min_keystrokes.append( get_length(lvl + 1, path + 'A') )
        if min_keystrokes:
            keystroke_total += min(min_keystrokes)
        else:
            keystroke_total += 1
    return keystroke_total

NUM_BOTS = 25
k_paths = get_paths(KEYPAD)
d_paths = get_paths(DPAD)

def solution_1(codes):

    total = 0
    for code in codes:
        num = int(code.lstrip('0')[:-1])
        length = get_length(0, code)
        total += num * length

    return total

def solution_2():
    return 0


if __name__ == "__main__":
    start = timer()
    codes = parse_input("puzzle_input/d21_input.txt")
    complexity = solution_1(codes)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {complexity}')

    # start = timer()
    # racetrack = parse_input("puzzle_input/d20_input.txt")
    # result = solution_2(racetrack, 100)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution1: {result}')

