import collections

class Coordinate():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

redgreen = set()
def set_redgreen():
    for coord in coords:
        redgreen.add((coord.x, coord.y))

    for i in range(1, len(coords)):
        c0 = coords[i-1]
        c1 = coords[i]
        if c0.x == c1.x:
            if c0.y > c1.y:
                c0, c1 = c1, c0
            y0, y1 = c0.y, c1.y
            while y0 < y1:
                redgreen.add((c0.x, y0))
                y0 += 1

        elif c0.y == c1.y:
            if c0.x > c1.x:
                c0, c1 = c1, c0

            x0, x1 = c0.x, c1.x
            while x0 < x1:
                redgreen.add((x0, c0.y))
                x0 += 1

    c0 = coords[0]
    c1 = coords[-1]
    if c0.x == c1.x:
        if c0.y > c1.y:
            c0, c1 = c1, c0
        y0, y1 = c0.y, c1.y
        while y0 < y1:
            redgreen.add((c0.x, y0))
            y0 += 1

    elif c0.y == c1.y:
        if c0.x > c1.x:
            c0, c1 = c1, c0

        x0, x1 = c0.x, c1.x
        while x0 < x1:
            redgreen.add((x0, c0.y))
            x0 += 1

# def get_known_inner():
#     p0, p1, p2 = coords[]
# 98149,50096
# 98149,51320
# 98283,51320
# 98283,52552
# 98418,52552

# 0, 0
# 0, 1224 V
# 134, 1224 >
# 134, 2456 V
# 269, 2456 >

fname = "2025/puzzle_input/d9p1_input.txt"
# fname = "2025/puzzle_input/d9p1_example.txt"
coords = []
# def read_input(filename):
maxx = maxy = 0
minx = miny = float("inf")
with open(fname, 'r', encoding="UTF-8") as f:
    for line in f:
        x, y = line[:-1].split(',')
        coords.append( Coordinate(int(x), int(y)) )
        maxx = max(maxx, int(x))
        maxy = max(maxy, int(y))
        minx = min(minx, int(x))
        miny = min(miny, int(y))

set_redgreen()
redgreenog = redgreen.copy()
known_green_inner = (8, 2)
# known_green_inner = (98282,51319)

def fill_redgreen(known_green_inner):
    q = [known_green_inner]
    nei = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # q = None
    while q:
        lq = len(q)
        for _ in range(lq):
            x, y = q.pop()
            if (x, y) in redgreen:
                continue
            redgreen.add((x, y))
            for dx, dy in nei:
                nx, ny = x + dx, y + dy
                if (0 <= nx <= maxx and 0 <= ny <= maxy):
                    q.append((nx, ny))

# for j in range(miny-2, maxy + 2):
#     line = []
#     for i in range(minx -2, maxx + 2):
#         if (i, j) in redgreen:
#             line.append('X')
#         else:
#             line.append('.')
#     print(''.join(line))

seen = set()
for coord in coords:
    nei = [(0, 1), (1, 0), (-1, 0), (-1, 0)]
    x, y = coord.x, coord.y
    for dx, dy in nei:
        redgreen = redgreenog.copy()
        print("filling")
        fill_redgreen((x + dx, y + dy))
        print("filled")
        largest_area = 0
        n = len(coords)
        for i in range(n):
            for j in range(i + 1, n):
                x1 = coords[i].x
                y1 = coords[i].y
                x2 = coords[j].x
                y2 = coords[j].y
                h = abs(y2 - y1) + 1
                w = abs(x2 - x1) + 1
                area = w * h
                # area is larger && both mirrored points are either red or between two red points
                if (area > largest_area):
                    mirrored1 = Coordinate(x2, y1)
                    mirrored2 = Coordinate(x1, y2)

                    if (x1, y2) in redgreen and (x2, y1) in redgreen:
                        largest_area = area
        seen.add(largest_area)         # printf("%lu: %d, %d ,, %d, %d\n", largest_area, x1, y1, x2, y2);
        print(largest_area)
print(seen)
