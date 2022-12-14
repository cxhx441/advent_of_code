in_file = "sample_input.txt"
in_file = "real_input.txt"
rocks = set()

lowest_rock_lvl = None
with open(in_file, 'r') as f:
    for line in f:
        line = line[:-1]
        line = line.split(" -> ")
        for i in range(len(line)-1):
            rock_start = line[i]
            rock_end = line[i+1]
            x0, y0 = rock_start.split(",")
            x1, y1 = rock_end.split(",")
            x0, y0 = int(x0), int(y0)
            x1, y1 = int(x1), int(y1)
            if x0 == x1:
                for j in range(abs(y0-y1)+1):
                    rocks.add((x0, min(y0, y1)+j))
            elif y0 == y1:
                for j in range(abs(x0-x1)+1):
                    rocks.add((min(x0, x1)+j, y0))

lowest_rock_lvl = None
for rock in rocks:
    if lowest_rock_lvl is None or rock[1] > lowest_rock_lvl:
        lowest_rock_lvl = rock[1]

SAND_SOURCE = (500, 0)
AT_REST = "AT_REST"
sand = set()
cur_sand = SAND_SOURCE
while cur_sand == AT_REST or cur_sand[1] < lowest_rock_lvl:
    if cur_sand == AT_REST:
        cur_sand = SAND_SOURCE
    x, y = cur_sand
    below = (x, y+1)
    down_left = (x-1, y+1)
    down_right = (x+1, y+1)
    # check spot below
    if below not in sand and below not in rocks:
        cur_sand = below
    # check spot left-down
    elif down_left not in sand and down_left not in rocks:
        cur_sand = down_left
    # check spot right-down
    elif down_right not in sand and down_right not in rocks:
        cur_sand = down_right
    else:
        sand.add(cur_sand)
        cur_sand = AT_REST

print(len(sand))
