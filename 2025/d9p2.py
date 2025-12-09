import collections

class Coordinate():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

vlines = set()
hlines = set()
green = set()
def set_green():
    for coord in coords:
        green.add((coord.x, coord.y))

    for i in range(1, len(coords)):
        c0 = coords[i-1]
        c1 = coords[i]
        if c0.x == c1.x:
            if c0.y > c1.y:
                c0, c1 = c1, c0
            y0, y1 = c0.y, c1.y
            while y0 < y1:
                green.add((c0.x, y0))
                vlines.add((c0.x, y0))
                y0 += 1

        elif c0.y == c1.y:
            if c0.x > c1.x:
                c0, c1 = c1, c0

            x0, x1 = c0.x, c1.x
            while x0 < x1:
                green.add((x0, c0.y))
                hlines.add((x0, c0.y))
                x0 += 1

    c0 = coords[0]
    c1 = coords[-1]
    if c0.x == c1.x:
        if c0.y > c1.y:
            c0, c1 = c1, c0
        y0, y1 = c0.y, c1.y
        while y0 < y1:
            green.add((c0.x, y0))
            vlines.add((c0.x, y0))
            y0 += 1

    elif c0.y == c1.y:
        if c0.x > c1.x:
            c0, c1 = c1, c0

        x0, x1 = c0.x, c1.x
        while x0 < x1:
            green.add((x0, c0.y))
            hlines.add((x0, c0.y))
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
fname = "2025/puzzle_input/d9p1_example.txt"
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

# print("lennnn")
# print(len(coords))
# print(len(set([ (coord.x, coord.y) for coord in coords])))
coordset = set([ (coord.x, coord.y) for coord in coords])

set_green()
# redgreenog = redgreen.copy()
# known_green_inner = (8, 2)
# known_green_inner = (98282,51319)

# def fill_redgreen(known_green_inner):
#     q = [known_green_inner]
#     nei = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     # q = None
#     while q:
#         lq = len(q)
#         for _ in range(lq):
#             x, y = q.pop()
#             if (x, y) in redgreen:
#                 continue
#             redgreen.add((x, y))
#             for dx, dy in nei:
#                 nx, ny = x + dx, y + dy
#                 if (0 <= nx <= maxx and 0 <= ny <= maxy):
#                     q.append((nx, ny))

for coord in coordset:
    if coord in vlines: vlines.remove(coord)
    if coord in hlines: hlines.remove(coord)

for j in range(miny-2, maxy + 2):
    line = []
    for i in range(minx -2, maxx + 2):
        if (i, j) in coordset:
            line.append('X')
        elif (i, j) in green:
            line.append('#')
        else:
            line.append('.')
    print(''.join(line))

print("v")
for j in range(miny-2, maxy + 2):
    line = []
    for i in range(minx -2, maxx + 2):
        if (i, j) in coordset and (i, j) in vlines:
            line.append('X')
        elif (i, j) in green and (i, j) in vlines:
            line.append('#')
        else:
            line.append('.')
    print(''.join(line))

print("h")
for j in range(miny-2, maxy + 2):
    line = []
    for i in range(minx -2, maxx + 2):
        if (i, j) in coordset and (i, j) in hlines:
            line.append('X')
        elif (i, j) in green and (i, j) in hlines:
            line.append('#')
        else:
            line.append('.')
    print(''.join(line))

# seen = set()
# for coord in coords:
    # nei = [(0, 1), (1, 0), (-1, 0), (-1, 0)]
    # x, y = coord.x, coord.y
    # for dx, dy in nei:
    # redgreen = redgreenog.copy()
    # print("filling")
    # # fill_redgreen((x + dx, y + dy))
    # print("filled")
def check_rectangle(c0, c1):
    ''' y |
        x --

        c0 . . .c0m
        .       .
        .       .
        c1m. . . c1
    '''

    def vedgecount(c):
        count1 = 0
        for x in range(c.x):
            if (x, c.y) in vlines:
                count1 += 1
        count2 = 0
        for x in range(maxx+10, c.x, -1):
            if (x, c.y) in vlines:
                count2 += 1
        return count1 % 2 == 1 and count2 % 2 == 1
    def hedgecount(c):
        count1 = 0
        for y in range(c.y):
            if (c.x, y) in hlines:
                count1 += 1

        count2 = 0
        for y in range(maxy+10, c.y, -1):
            if (c.x, y) in hlines:
                count2 += 1

        return count1 % 2 == 1 and count2 % 2 == 1


    if (c0.x**2 + c0.y**2) > (c1.x**2 + c1.y**2):
        c0, c1 = c1, c0

    c0m = Coordinate(c1.x, c0.y)
    c1m = Coordinate(c0.x, c1.y)

    if not ( (c0m.x, c0m.y) in green | coordset or vedgecount(c0m) and hedgecount(c0m) ) :
        return False
    if not ( (c1m.x, c1m.y) in green | coordset or vedgecount(c1m) and hedgecount(c1m) ) :
        return False

    print("")
    for j in range(miny-2, maxy + 2):
        line = []
        for i in range(minx -2, maxx + 2):
            if (i, j) == (c0.x, c0.y):
                line.append('1')
            elif (i, j) == (c0m.x, c0m.y):
                line.append('2')
            elif (i, j) == (c1.x, c1.y):
                line.append('3')
            elif (i, j) == (c1m.x, c1m.y):
                line.append('4')
            elif (i, j) in coordset:
                line.append('X')
            elif (i, j) in green:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))

    # for x in range(c0.x, c0m.x + 1): # c0 -> c0m
    #     if (x, c0.y) in vlines:
    #         print("fail")
    #         return False
    # for y in range(c0.y, c1m.y + 1): # c0 -> c1m
    #     if (c0.x, y) in hlines:
    #         print("fail")
    #         return False
    # for x in range(c1m.x, c1.x + 1): # c1m -> c1
    #     if (x, c1m.y) in vlines:
    #         print("fail")
    #         return False
    # for y in range(c0m.y, c1.y + 1): # c0m -> c1
    #     if (c0m.x, y) in hlines:
    #         print("fail")
    #         return False

    print("succeed")
    return True




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
            if check_rectangle(coords[i], coords[j]):
                largest_area = area
            # mirrored1 = Coordinate(x2, y1)
            # mirrored2 = Coordinate(x1, y2)

            # if (x1, y2) in redgreen and (x2, y1) in redgreen:
            #     largest_area = area
# seen.add(largest_area)         # printf("%lu: %d, %d ,, %d, %d\n", largest_area, x1, y1, x2, y2);
print(largest_area)
# print(seen)
