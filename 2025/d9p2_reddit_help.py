from typing import NamedTuple
from itertools import combinations, chain, pairwise
from collections import defaultdict
from bisect import bisect

class Point(NamedTuple):
    x : int
    y : int


FNAME = "2025/puzzle_input/d9p1_example.txt"
FNAME = "2025/puzzle_input/d9p1_input.txt"

def get_reds():
    point_list = []
    with open(FNAME, 'r', encoding="UTF-8") as f:
        for line in f:
            x, y = map(int, line[:-1].split(','))
            point_list.append( Point(x, y) )
    return point_list


def get_greens():
    point_list = []
    for p0, p1 in pairwise( chain(reds, [reds[0]]) ):
        for point in generate_straight_lines(p0, p1):
            point_list.append(point)
    return point_list


def calculate_area(p0, p1):
    w = 1 + abs(p0.x - p1.x)
    h = 1 + abs(p0.y - p1.y)
    return w * h


def generate_straight_lines(p0, p1):
    if p0.y == p1.y:
        x_min = min(p0.x, p1.x)
        x_max = max(p0.x, p1.x)
        for x in range(x_min + 1, x_max):
            yield Point(x, p0.y)
    elif p0.x == p1.x:
        y_min = min(p0.y, p1.y)
        y_max = max(p0.y, p1.y)
        for y in range(y_min + 1, y_max):
            yield Point(p0.x, y)
    else:
        raise ValueError("Only Horizontal and Vertical Lines Supported.")

reds = get_reds()

decreasing_red_pairs = sorted( # generator
    ( (calculate_area(*pair), pair) for pair in combinations(reds, 2) ),
    reverse=True)

greens = get_greens()

y_lists = defaultdict(list)
x_lists = defaultdict(list)
for p in chain(reds, greens):
    y_lists[p.x].append(p.y)
    x_lists[p.y].append(p.x)

for p in chain(reds, greens):
    y_lists[p.x].sort()
    x_lists[p.y].sort()


def valid_rectangle(p0, p1):
    # need to shrink rectangle by 1 to avoid touching an edge
    x_min = min(p0.x, p1.x) + 1
    x_max = max(p0.x, p1.x) - 1
    y_min = min(p0.y, p1.y) + 1
    y_max = max(p0.y, p1.y) - 1

    if bisect(y_lists[x_min], y_min) != bisect(y_lists[x_min], y_max):
        return False
    if bisect(y_lists[x_max], y_min) != bisect(y_lists[x_max], y_max):
        return False
    if bisect(x_lists[y_min], x_min) != bisect(x_lists[y_min], x_max):
        return False
    if bisect(x_lists[y_max], x_min) != bisect(x_lists[y_max], x_max):
        return False
    return True

largest_area_p2 = 0
for area, pair in decreasing_red_pairs:
    if valid_rectangle(*pair):
        largest_area_p2 = area
        break

largest_area_p1, _ = decreasing_red_pairs[0]
if "example" in FNAME:
    print(f"part1 = {largest_area_p1} | Correct: {largest_area_p1 == 50}")
    print(f"part2 = {largest_area_p2} | Correct: {largest_area_p2 == 24}")
else:
    print(f"part1 = {largest_area_p1} | Correct: {largest_area_p1 == 4746238001}")
    print(f"part2 = {largest_area_p2} | Correct: {largest_area_p2 == 1552139370}")
