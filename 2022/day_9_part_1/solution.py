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
        return (h[0], h[1]-1)
    elif direction == 'R':
        return (h[0], h[1]+1)
    elif direction == 'U':
        return (h[0]-1, h[1])
    elif direction == 'D':
        return (h[0]+1, h[1])


# keep track, in a set, the positions that T visits
t = h = (0, 0)
t_visited = set()
for command in queue:
    direction, count = command
    for increment in range(count):
        t_visited.add(t)
        print(t)
        h_next = get_next(h, direction)

        # if H is on top of T, move h
        if h == t or h_next == t:
            h = h_next
        # if H is diagonal, and then H moves and they are not touching, move T to where H was
        elif are_immidiately_diagonal(h, t):
            if not are_adjacent(h_next, t):
                t = h
                h = h_next
            elif are_adjacent(h_next, t):
                h = h_next
        # if H is in a cardinal direction, then moves,
        #           if H is still in a cardinal direction, move T to where H was
        #           if H is now diagonal, don't move T
        elif are_immidiately_updownleftright(h, t):
            if are_updownleftright_non_adjacent(h_next, t):
                t = h
                h = h_next
            elif are_immidiately_diagonal(h_next, t):
                h = h_next
    t_visited.add(t)


print(len(t_visited))
