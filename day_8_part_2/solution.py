infile = "sample_input.txt"
infile = "real_input.txt"
forest = []
with open(infile, 'r') as f:
    for line in f:
        forest.append([int(x) for x in [*line[:-1]]])

# how many spaces are there before there is something >= than me
# init grids
view_dist_up = [[[0]*10 for _ in range(len(forest[0]))] for _ in range(len(forest))]
view_dist_down = [[[0]*10 for _ in range(len(forest[0]))] for _ in range(len(forest))]
view_dist_left = [[[0]*10 for _ in range(len(forest[0]))] for _ in range(len(forest))]
view_dist_right = [[[0]*10 for _ in range(len(forest[0]))] for _ in range(len(forest))]

# populate grids
# each coordinate holds a len(list) == 10 where the index repr the tree's height
# and the value represents the view distance in that direction for that tree's height
for col in range(len(forest[0])):
    for row in range(1, len(forest)):
        tree_above = forest[row-1][col]
        for height in range(10):
            if height > tree_above:
                view_dist_up[row][col][height] += view_dist_up[row-1][col][height] + 1
            else:
                view_dist_up[row][col][height] = 1

for col in range(len(forest[0])):
    for row in range(len(forest)-2, -1, -1):
        tree_below = forest[row+1][col]
        for height in range(10):
            if height > tree_below:
                view_dist_down[row][col][height] += view_dist_down[row+1][col][height] + 1
            else:
                view_dist_down[row][col][height] = 1

for row in range(len(forest)):
    for col in range(1, len(forest[0])):
        tree_left = forest[row][col-1]
        for height in range(10):
            if height > tree_left:
                view_dist_left[row][col][height] += view_dist_left[row][col-1][height] + 1
            else:
                view_dist_left[row][col][height] = 1

for row in range(len(forest)):
    for col in range(len(forest[0])-2, -1, -1):
        tree_right = forest[row][col+1]
        for height in range(10):
            if height > tree_right:
                view_dist_right[row][col][height] += view_dist_right[row][col+1][height] + 1
            else:
                view_dist_right[row][col][height] = 1

# calc scenic score
cur_max = 0
for row in range(len(forest)):
    for col in range(len(forest[0])):
        height = forest[row][col]

        up = view_dist_up[row][col][height]
        down = view_dist_down[row][col][height]
        left = view_dist_left[row][col][height]
        right = view_dist_right[row][col][height]

        this_max = up * down * left * right
        cur_max = max(cur_max, this_max)

print(cur_max)
