infile = "real_input.txt"
infile = "sample_input.txt"
with open(infile, 'r') as f:
    queue = []
    for line in f:
        direction, count = line[:-1].split(' ')
        queue.append((direction, int(count)))

def are_immidiately_diagonal(t, h):
    # up-left # up-right # down-left # down-right
    if h[0] == t[0] - 1 and h[1] == t[1] - 1 or \
       h[0] == t[0] - 1 and h[1] == t[1] + 1 or \
       h[0] == t[0] + 1 and h[1] == t[1] - 1 or \
       h[0] == t[0] + 1 and h[1] == t[1] + 1:
       return True
    return False

def are_immidiately_updownleftright(h, t):
    #up, down, left, right
    if h[0] == t[0] - 1 and h[1] == t[1] or \
       h[0] == t[0] + 1 and h[1] == t[1] or \
       h[0] == t[0] and h[1] == t[1] - 1 or \
       h[0] == t[0] and h[1] == t[1] + 1:
       return True
    return False

def are_updownleftright_non_adjacent(h, t):
    #up, down, left, right
    if h[0] == t[0] - 2 and h[1] == t[1] or \
       h[0] == t[0] + 2 and h[1] == t[1] or \
       h[0] == t[0] and h[1] == t[1] - 2 or \
       h[0] == t[0] and h[1] == t[1] + 2:
       return True
    return False


def are_adjacent(h, t):
    # up-left
    if are_immidiately_diagonal(h, t) or are_immidiately_updownleftright(h, t):
       return True
    return False

def get_next(h, direction):
    if direction == 'L':
        return list((h[0], h[1]-1))
    elif direction == 'R':
        return list((h[0], h[1]+1))
    elif direction == 'U':
        return list((h[0]-1, h[1]))
    elif direction == 'D':
        return list((h[0]+1, h[1]))
    elif direction == 'up_right':
        return list((h[0]-1, h[1]+1))
    elif direction == 'up_left':
        return list((h[0]-1, h[1]-1))
    elif direction == 'down_right':
        return list((h[0]+1, h[1]+1))
    elif direction == 'down_left':
        return list((h[0]+1, h[1]-1))

def get_direction(h, t):
    if t[0]-1 == h[0] and t[1] == h[1]: return 'U'
    elif t[0]+1 == h[0] and t[1] == h[1]: return 'D'
    elif t[0] == h[0] and t[1]-1 == h[1]: return 'L'
    elif t[0] == h[0] and t[1]+1 == h[1]: return 'R'
    elif t[0]-1 == h[0] and t[1]+1 == h[1]: return 'up_right'
    elif t[0]-1 == h[0] and t[1]-1 == h[1]: return 'up_left'
    elif t[0]+1 == h[0] and t[1]+1 == h[1]: return 'down_right'
    elif t[0]+1 == h[0] and t[1]-1 == h[1]: return 'down_left'

def are_diagonal_non_immidiate(h, t):
    #up_right - right
    if h[0] == t[0] - 1 and h[1] == t[1] + 2: return True
    #up_right - up
    if h[0] == t[0] - 2 and h[1] == t[1] + 1: return True
    #down_right - right
    if h[0] == t[0] + 1 and h[1] == t[1] + 2: return True
    #down_right - down
    if h[0] == t[0] + 2 and h[1] == t[1] + 1: return True

    #up_left - left
    if h[0] == t[0] - 1 and h[1] == t[1] - 2: return True
    #up_left - up
    if h[0] == t[0] - 2 and h[1] == t[1] - 1: return True
    #down_left - left
    if h[0] == t[0] + 1 and h[1] == t[1] - 2: return True
    #down_left - down
    if h[0] == t[0] + 2 and h[1] == t[1] - 1: return True

    return False

def update_rope(prev_rope, rope):
    # if H is on top of T, move h
    for i in range(len(rope)):
        if prev_rope[i] != rope[i]:
            h = rope[i]
            t = prev_rope[i]
            print_map(rope)
            print()
            direction = get_direction(h, t)
            


def print_map(rope):
    mapp = [['.']*6 for _ in range(5)]
    for i in range(len(rope)-1, -1, -1):
        row, col = rope[i]
        mapp[row][col] = str(i)

    for x in mapp:
        print(x)

def move_knot(knot, direction):
    if direction == 'U': knot[0] -= 1
    if direction == 'D': knot[0] += 1
    if direction == 'L': knot[1] -= 1
    if direction == 'R': knot[1] += 1
    if direction == 'up_right':
        knot[0] -= 1
        knot[1] += 1
    if direction == 'down_right':
        knot[0] += 1
        knot[1] += 1
    if direction == 'up_left':
        knot[0] -= 1
        knot[1] -= 1
    if direction == 'down_left':
        knot[0] += 1
        knot[1] -= 1

# keep track, in a set, the positions that T visits
rope = [[4, 0]]*10
t_visited = set()
for command in queue:
    direction, count = command
    for increment in range(count):
        t_visited.add(tuple(rope[9]))
        prev_rope = rope.copy()
        move_knot(rope[0], direction)
        update_rope(prev_rope, rope)
        t_visited.add(tuple(rope[9]))
        # print(tuple(rope[9]))
    t_visited.add(tuple(rope[9]))


print(len(t_visited))
