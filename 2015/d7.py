
from collections import defaultdict

BITMASK16 = 0xFFFF

def process(l, op, r):
    if op == "NOT":
        return r ^ BITMASK16
    elif op == "AND":
        return (l & r) & BITMASK16
    elif op == "OR":
        return (l | r) & BITMASK16
    elif op == "LSHIFT":
        return (l << r) & BITMASK16
    elif op == "RSHIFT":
        return (l >> r) & BITMASK16

if __name__ == "__main__":
    indegrees = defaultdict(int)
    wires = defaultdict(None)
    stack = []
    adj_map = defaultdict(list)

    # FNAME = "2015/puzzle_input/d7_expy.txt"
    FNAME = "2015/puzzle_input/d7py.txt"
    with open(FNAME, 'r', encoding="UTF-8") as f:
        # grid = []
        for line in f:
            w_input, w3 = line[:-1].split(' -> ')
            if w_input.isnumeric():
                wires[w3] = int(w_input)
                stack.append(w3)
            elif "NOT" in w_input:
                op, w1 = w_input.split(" ")
                adj_map[w1].append(w3)
                indegrees[w3] += 1
                wires[w3] = ('_', op, w1)
            else:
                l, op, r = w_input.split(" ")
                if l.isnumeric() and r.isnumeric():
                    wires[w3] = process(l, op, r)
                else:
                    wires[w3] = (l, op, r)
                    if not l.isnumeric():
                        adj_map[l].append(w3)
                        indegrees[w3] += 1
                    if not r.isnumeric():
                        adj_map[r].append(w3)
                        indegrees[w3] += 1

    while stack:
        w = stack.pop()
        for nei in adj_map[w]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                l, op, r = wires[nei]
                if op != "NOT":
                    l = int(l) if l.isnumeric() else wires[l]
                r = int(r) if r.isnumeric() else wires[r]
                wires[nei] = process(l, op, r)
                stack.append(nei)

    for k, v in sorted(wires.items()):
        print(f"{k}: {v}")








# return grid
