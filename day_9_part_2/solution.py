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

    elif t[0]-1 == h[0] and t[1]+2 == h[1]: return 'up_right_right'
    elif t[0]-1 == h[0] and t[1]-2 == h[1]: return 'up_left_left'
    elif t[0]+1 == h[0] and t[1]+2 == h[1]: return 'down_right_right'
    elif t[0]+1 == h[0] and t[1]-2 == h[1]: return 'down_left_left'
    elif t[0]-2 == h[0] and t[1]+1 == h[1]: return 'up_right_up'
    elif t[0]-2 == h[0] and t[1]-1 == h[1]: return 'up_left_up'
    elif t[0]+2 == h[0] and t[1]+1 == h[1]: return 'down_right_down'
    elif t[0]+2 == h[0] and t[1]-1 == h[1]: return 'down_left_down'

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

def update_rope(rope, k1, k2, h_prev, direction):
    # if H is on top of T, move h
    h = rope[k1].copy()
    t = rope[k2].copy()
    # direction = get_direction(h, t)
    if h_prev == None:
        h_next = get_next(h, direction)
        # if H is on top of T, move h
        if h == t or h_next == t:
            rope[k1] = h_next.copy()
            return False
        # if H is diagonal, and then H moves and they are not touching, move T to where H was
        elif are_immidiately_diagonal(h, t):
            if not are_adjacent(h_next, t):
                t_prev = t.copy()
                rope[k2] = h.copy()
                rope[k1] = h_next.copy()
                return t_prev
            elif are_adjacent(h_next, t):
                rope[k1] = h_next.copy()
                return False
        # if H is in a cardinal direction, then moves,
        #           if H is still in a cardinal direction, move T to where H was
        #           if H is now diagonal, don't move T
        elif are_immidiately_updownleftright(h, t):
            if are_updownleftright_non_adjacent(h_next, t):
                t_prev = t.copy()
                rope[k2] = h.copy()
                rope[k1] = h_next.copy()
                return t_prev
            elif are_immidiately_diagonal(h_next, t):
                rope[k1] = h_next.copy()
                return False
    else:
        h_next = h.copy()
        h = h_prev.copy()
        # if H is on top of T, move h
        if h == t or h_next == t:
            return False
        # if H is diagonal, and then H moves and they are not touching, move T to where H was
        elif are_immidiately_diagonal(h, t):
            if not are_adjacent(h_next, t):
                t_prev = t.copy()
                rope[k2] = h.copy()
                return t_prev
            elif are_adjacent(h_next, t):
                return False
        # if H is in a cardinal direction, then moves,
        #           if H is still in a cardinal direction, move T to where H was
        #           if H is now diagonal, don't move T
        elif are_immidiately_updownleftright(h, t):
            if are_updownleftright_non_adjacent(h_next, t):
                t_prev = t.copy()
                rope[k2] = h.copy()
                return t_prev
            elif are_immidiately_diagonal(h_next, t):
                return False
            elif are_diagonal_non_immidiate(h_next, t):
                direction = get_direction(h_next, t)
                t_prev = t.copy()
                move_knot(rope[k2], direction)
                return t_prev.copy()




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
    if direction == 'up_right_right':
        knot[0] -= 1
        knot[1] += 2
    if direction == 'down_right_right':
        knot[0] += 1
        knot[1] += 2
    if direction == 'up_left_left':
        knot[0] -= 1
        knot[1] -= 2
    if direction == 'down_left_left':
        knot[0] += 1
        knot[1] -= 2
    if direction == 'up_right_up':
        knot[0] -= 2
        knot[1] += 1
    if direction == 'down_right_down':
        knot[0] += 2
        knot[1] += 1
    if direction == 'up_left_up':
        knot[0] -= 2
        knot[1] -= 1
    if direction == 'down_left_down':
        knot[0] += 2
        knot[1] -= 1

# keep track, in a set, the positions that T visits
rope = [[4, 0]]*10
t_visited = set()
print_map(rope)
for command in queue:
    direction, count = command
    for increment in range(count):
        print()
        t_visited.add(tuple(rope[9]))
        k1 = 0
        k2 = 1
        k1_prev = update_rope(rope, k1, k2, None, direction)
        print_map(rope)
        i = 1
        while i <= len(rope)-2 and k1_prev:
            k1 = i
            k2 = i+1
            k1_prev = update_rope(rope, k1, k2, k1_prev, direction)
            print_map(rope)
            i += 1
        t_visited.add(tuple(rope[9]))
        # print(tuple(rope[9]))
    t_visited.add(tuple(rope[9]))


print(len(t_visited))
