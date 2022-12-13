from collections import deque
import queue
import math

# bfs approach to get from puzzle[0][0] to puzzle[-1][-1]
def get_valid_neighbors(topo_map, row, col):
    neighbors = []
    if row-1 in range(len(topo_map)): neighbors.append((row-1, col)) # up
    if row+1 in range(len(topo_map)): neighbors.append((row+1, col)) # down
    if col-1 in range(len(topo_map[0])): neighbors.append((row, col-1)) # left
    if col+1 in range(len(topo_map[0])): neighbors.append((row, col+1)) # right
    return neighbors


infile = "sample_input.txt"
infile = "real_input.txt"
topo_map = []
with open(infile, 'r') as f:
    for line in f:
        topo_map.append([x for x in line[:-1]])

def bfs(topo_map, start):
    queue = deque()
    queue.appendleft((0, start[0], start[1]))
    visited = set()

    while queue:
        cur_dist, row, col = queue.pop()

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for neighbor in get_valid_neighbors(topo_map, row, col):
            n_row, n_col = neighbor
            if (n_row, n_col) not in visited:
                climb_height = ord(topo_map[n_row][n_col]) - ord(topo_map[row][col])
                if climb_height >= -1:
                    if topo_map[n_row][n_col] == 'a':
                        return cur_dist+1
                    queue.appendleft((cur_dist+1, n_row, n_col))


# get location of start and end locations
start = to_a = None
for row in range(len(topo_map)):
    for col in range(len(topo_map[0])):
        if start is None and topo_map[row][col] == 'E':
            start = (row, col)
        if to_a is None and topo_map[row][col] == 'S':
            to_a = (row, col)

# modify start and end locations
topo_map[start[0]][start[1]] = 'z'
topo_map[to_a[0]][to_a[1]] = 'a'
dist = bfs(topo_map, start)
print(dist)



