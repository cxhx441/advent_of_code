import collections
from PIL import Image

class Coordinate():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

def create_image():
    print("creating_image")
    img = Image.new('RGB', (maxx+10, maxy+10), color='black')
    pixels = img.load()
    for coord in redgreen:
        pixels[coord[0], coord[1]] = (255, 255, 255)
    img.save('my new_image.png')
    print("image_created")



vlines = set()
hlines = set()
greenset = set()
def set_green():
    # for coord in red:
    #     greenset.add((coord.x, coord.y))

    for i in range(1, len(red)):
        c0 = red[i-1]
        c1 = red[i]
        if c0.x == c1.x:
            if c0.y > c1.y:
                c0, c1 = c1, c0
            y0, y1 = c0.y, c1.y
            y0 += 1
            while y0 < y1:
                greenset.add((c0.x, y0))
                vlines.add((c0.x, y0))
                y0 += 1

        elif c0.y == c1.y:
            if c0.x > c1.x:
                c0, c1 = c1, c0

            x0, x1 = c0.x, c1.x
            x0 += 1
            while x0 < x1:
                greenset.add((x0, c0.y))
                hlines.add((x0, c0.y))
                x0 += 1

    c0 = red[0]
    c1 = red[-1]
    if c0.x == c1.x:
        if c0.y > c1.y:
            c0, c1 = c1, c0
        y0, y1 = c0.y, c1.y
        y0 += 1
        while y0 < y1:
            greenset.add((c0.x, y0))
            vlines.add((c0.x, y0))
            y0 += 1

    elif c0.y == c1.y:
        if c0.x > c1.x:
            c0, c1 = c1, c0

        x0, x1 = c0.x, c1.x
        x0 += 1
        while x0 < x1:
            greenset.add((x0, c0.y))
            hlines.add((x0, c0.y))
            x0 += 1

fname = "2025/puzzle_input/d9p1_input.txt"
# fname = "2025/puzzle_input/d9p1_example.txt"
red = []
maxx = maxy = 0
minx = miny = float("inf")
with open(fname, 'r', encoding="UTF-8") as f:
    for line in f:
        x, y = line[:-1].split(',')
        red.append( Coordinate(int(x), int(y)) )
        maxx = max(maxx, int(x))
        maxy = max(maxy, int(y))
        minx = min(minx, int(x))
        miny = min(miny, int(y))

# print("lennnn")
# print(len(red))
# print(len(set([ (coord.x, coord.y) for coord in red])))
redset = set([ (coord.x, coord.y) for coord in red])
set_green()
redgreen = redset | greenset
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

# print("checking")
# for i in range(2, len(red)):
#     if red[i-2].x == red[i-1].x == red[i].x:
#         print(red[i-2], red[i-1], red[i])
#     if red[i-2].y == red[i-1].y == red[i].y:
#         print(red[i-2], red[i-1], red[i])

for coord in redset:
    if coord in vlines: vlines.remove(coord)
    if coord in hlines: hlines.remove(coord)
    if coord in greenset: greenset.remove(coord)

printing = False
if (printing):
    for j in range(miny-2, maxy + 2):
        line = []
        for i in range(minx -2, maxx + 2):
            if (i, j) in greenset:
                line.append('#')
            elif (i, j) in redset:
                line.append('X')
            else:
                line.append('.')
        print(''.join(line))

    print("v")
    for j in range(miny-2, maxy + 2):
        line = []
        for i in range(minx -2, maxx + 2):
            if (i, j) in redset and (i, j) in vlines:
                line.append('X')
            elif (i, j) in greenset and (i, j) in vlines:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))

    print("h")
    for j in range(miny-2, maxy + 2):
        line = []
        for i in range(minx -2, maxx + 2):
            if (i, j) in redset and (i, j) in hlines:
                line.append('X')
            elif (i, j) in greenset and (i, j) in hlines:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))

# seen = set()
# for coord in red:
    # nei = [(0, 1), (1, 0), (-1, 0), (-1, 0)]
    # x, y = coord.x, coord.y
    # for dx, dy in nei:
    # redgreen = redgreenog.copy()
    # print("filling")
    # # fill_redgreen((x + dx, y + dy))
    # print("filled")
all_vlines = vlines | redset
alledges = greenset | redset
new_vlines = []
for i in range(1, len(red)):
    if red[i-1].x == red[i].x:
        x, top, bottom = red[i-1].x, red[i-1].y, red[i].y
        if top > bottom:
            top, bottom = bottom, top
        new_vlines.append((x, top, bottom))

if red[0].x == red[-1].x:
    x, top, bottom = red[0].x, red[0].y, red[-1].y
    if top > bottom:
        top, bottom = bottom, top
    new_vlines.append((x, top, bottom))



def check_point(c):
    if (c.x, c.y) in alledges:
        return True
    count = 0
    for x, top, bottom in new_vlines:
        if x < c.x and top <= c.y < bottom:
            count += 1
    return count % 2 == 1

def check_rectangle(c0, c1):
    ''' y |
        x --

        c0 . . .c0m
        .       .
        .       .
        c1m. . . c1
    '''

    if (c0.x**2 + c0.y**2) > (c1.x**2 + c1.y**2):
        c0, c1 = c1, c0

    c0m = Coordinate(c1.x, c0.y)
    c1m = Coordinate(c0.x, c1.y)

    for x in range(c0.x, c0m.x + 1):
        if not check_point(Coordinate(x, c0.y)):
            return False
    for x in range(c1m.x, c1.x + 1):
        if not check_point(Coordinate(x, c1m.y)):
            return False
    for y in range(c0.y, c1m.y + 1):
        if not check_point(Coordinate(c0.x, y)):
            return False
    for y in range(c0m.y, c1.y + 1):
        if not check_point(Coordinate(c0m.x, y)):
            return False

    return True

# create_image()

largest_area = 0
n = len(red)
for i in range(n):
    # 94539,48701
    # for j in range(i + 1, n):
    x1 = red[i].x
    y1 = red[i].y
    # x2 = red[j].x
    # y2 = red[j].y
    # x2, y2 = 94539, 48701
    # if y1 > y2: continue
    x2, y2 = 94539,50089
    if y1 < y2: continue
    h = abs(y2 - y1) + 1
    w = abs(x2 - x1) + 1
    area = w * h
    # area is larger && both mirrored points are either red or between two red points
    if (area > largest_area):
        # if check_rectangle(red[i], red[j]):
        if check_rectangle(red[i], Coordinate(x2, y2)):
            largest_area = area
            print(f"largest_area, area: {largest_area}, {area}")
        # mirrored1 = Coordinate(x2, y1)
        # mirrored2 = Coordinate(x1, y2)

        # if (x1, y2) in redgreen and (x2, y1) in redgreen:
        #     largest_area = area
# seen.add(largest_area)         # printf("%lu: %d, %d ,, %d, %d\n", largest_area, x1, y1, x2, y2);
print("prev = 1472215589")
print(largest_area)
# print(seen)
