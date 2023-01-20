infile = "sample_input.txt"
infile = "real_input.txt"
infile = "sample_input2.txt"
with open(infile, 'r') as f:
    queue = []
    for line in f:
        direction, count = line[:-1].split(' ')
        queue.append((direction, int(count)))

def update_rope(h, t):
    row, col = h[0] - t[0], h[1] - t[1]

    # if on same spot
    if row == 0 and col == 0:
        return

    # if 1 axis different
    elif row * col == 0:
        if abs(row + col) == 1: # they are next to each other
            return
        elif row == 2: t[0] += 1 # down w space
        elif row == -2: t[0] -= 1 # up w space
        elif col == 2: t[1] += 1 # right w space
        elif col == -2: t[1] -= 1 # left w space

    # if 2 axis different and product 2, aka if were diagonal and then head moved in cardinal dir
    elif abs(row*col) == 2:
        if row == -2: t[0], t[1] = h[0]+1, h[1] # up
        elif row == 2: t[0], t[1] = h[0]-1, h[1] # down
        elif col == -2: t[0], t[1] = h[0], h[1]+1 # left
        elif col == 2: t[0], t[1] = h[0], h[1]-1 # right

    # if 2 different axis and product 4
    elif abs(row*col) == 4:
        # rope.print_rope()
        if row == -2 and col == 2: t[0], t[1] = h[0]+1, h[1]-1 # up right
        elif row == 2 and col == 2: t[0], t[1] = h[0]-1, h[1]-1 # down right
        elif row == -2 and col == -2: t[0], t[1] = h[0]+1, h[1]+1 # up left
        elif row == 2 and col == -2: t[0], t[1] = h[0]-1, h[1]+1 #  down left




    # if 2 axis different and product 4






# keep track, in a set, the positions that T visits
class rope_cl():
    def __init__(self, rows, cols, start_row, start_col):
        self.knots = [[start_row, start_col] for _ in range(10)]
        self.rows = rows
        self.cols = cols


    # def __repr__(self):
    #     mapp = [['.']*6 for _ in range(5)]
    #     for i in range(len(self.knots)-1, -1, -1):
    #         row, col = self.knots[i]
    #         mapp[row][col] = str(i)

    #     return_str = ''
    #     for x in mapp:
    #         return_str += ''.join(x)
    #         return_str += '\n'
    #     return return_str

    def print_rope(self):
        mapp = [['.']*self.cols for _ in range(self.rows)]
        for i in range(len(self.knots)-1, -1, -1):
            row, col = self.knots[i]
            if i == 0:
                s = 'H'
            else:
                s = str(i)
            mapp[row][col] = s

        return_str = ''
        for x in mapp:
            return_str += ''.join(x)
            return_str += '\n'
        print(return_str)
        # return return_str


rope = rope_cl(35, 35, 15, 15)
move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
t_visited = set()
# rope.print_rope()
for command in queue:
    direction, count = command
    for _ in range(count):
        # move head
        h = rope.knots[0]
        h[0] += move[direction][0]
        h[1] += move[direction][1]
        # update rest of rope
        for i in range(len(rope.knots)-1):
            # rope.print_rope()
            update_rope(rope.knots[i], rope.knots[i+1])
        t_visited.add(tuple(rope.knots[-1]))
        # rope.print_rope()

    t_visited.add(tuple(rope.knots[-1]))


print(len(t_visited))
