infile = "sample_input.txt"
infile = "real_input.txt"
forest = []
with open(infile, 'r') as f:
    for line in f:
        forest.append([int(x) for x in [*line[:-1]]])

# init grids
view_from_top = [[0 for _ in range(len(forest[0]))] for _ in range(len(forest))]
view_from_bottom = [[0 for _ in range(len(forest[0]))] for _ in range(len(forest))]
view_from_left = [[0 for _ in range(len(forest[0]))] for _ in range(len(forest))]
view_from_right = [[0 for _ in range(len(forest[0]))] for _ in range(len(forest))]

# populate grids such that each el repr the # of trees
#    you can see from that direct to the index
for col in range(len(forest[0])):
    for row in range(1, len(forest)):
        view_from_top[row][col] = max(view_from_top[row-1][col], forest[row-1][col])

for col in range(len(forest[0])):
    for row in range(len(forest)-2, -1, -1):
        view_from_bottom[row][col] = max(view_from_bottom[row+1][col], forest[row+1][col])

for row in range(len(forest)):
    for col in range(1, len(forest[0])):
        view_from_left[row][col] = max(view_from_left[row][col-1], forest[row][col-1])

for row in range(len(forest)):
    for col in range(len(forest[0])-2, -1, -1):
        view_from_right[row][col] = max(view_from_right[row][col+1], forest[row][col+1])

# calc visible trees
visible_trees = 0
for col in range(len(forest[0])):
    for row in range(len(forest)):
        tree = forest[row][col]
        left = view_from_left[row][col]
        right = view_from_right[row][col]
        top = view_from_top[row][col]
        bottom = view_from_bottom[row][col]

        if row in (0,len(forest)-1) or col in (0, len(forest[0])-1) or \
           tree > left or \
           tree > right or \
           tree > top or \
           tree > bottom:

           visible_trees += 1

print(visible_trees)


