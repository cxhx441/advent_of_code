import math

filename = "2025/puzzle_input/d8p1_input.txt"
LIMIT = 1000

filename = "2025/puzzle_input/d8p1_example.txt"
LIMIT = 10


def find(target):
    seen = set()
    cur = target

    while uf[cur] >= 0:
        seen.add(cur)
        cur = uf[cur]

    parent = cur

    for node in seen:
        uf[node] = parent

    return parent

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a == parent_b:
        return False

    rank_a = -uf[parent_a]
    rank_b = -uf[parent_b]
    rank_ab = rank_a + rank_b

    if rank_a >= rank_b:
        uf[parent_a] = -rank_ab
        uf[parent_b] = parent_a
    else:
        uf[parent_b] = -rank_ab
        uf[parent_a] = parent_b

    return True

def get_len(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return math.sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2 )



coords = []
# def read_input(filename):
with open(filename, 'r', encoding="UTF-8") as f:
    # grid = []
    for line in f:
        x, y, z = line[:-1].split(',')
        coords.append((int(x), int(y), int(z)))
# return grid

edges = []
for a in range(len(coords)):
    for b in range(a + 1, len(coords)):
        edges.append( (get_len(coords[a], coords[b]), a, b) )
edges.sort(reverse=True)

uf = [-1] * len(coords)
merged = 0
# while (merged < LIMIT and edges != []):
for i in range(LIMIT):
    length, a, b = edges.pop()

    if union(a, b) is True:
        merged += 1

print(uf)
uf.sort()
print()
print(uf)

print(-uf[0] * -uf[1] * -uf[2])


