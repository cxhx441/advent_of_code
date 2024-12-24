from timeit import default_timer as timer
import collections
import re
import itertools

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        nodes = dict()
        in_degrees = collections.defaultdict(set)
        nodes_and_gates = dict()
        edges = collections.defaultdict(set)

        data = f.read().strip()
        inits, gates = data.split('\n\n')
        inits = inits.split('\n')
        gates = gates.split('\n')

        for gate in gates:
            node0, gate, node1, arrow, node2 = gate.split(' ')
            # nodes[node0] = None
            # nodes[node1] = None
            # nodes[node2] = None
            nodes_and_gates[node2] = (node0, gate, node1)
            in_degrees[node2].add(node0)
            in_degrees[node2].add(node1)
            edges[node0].add(node2)
            edges[node1].add(node2)

        q = collections.deque()
        for init in inits:
            node, val = init.split(': ')
            nodes[node] = int(val)
            q.append(node)

    return nodes, nodes_and_gates, in_degrees, edges, q

def solve(cur, nodes, ngc):
    if cur in nodes:
        return nodes[cur]

    node0, gate, node1 = ngc[cur]
    if gate == "AND":
        if nodes[node0] and nodes[node1]:
            result = 1
        else:
            result = 0
    elif gate == "OR":
        if nodes[node0] or nodes[node1]:
            result = 1
        else:
            result= 0
    elif gate == "XOR":
        if nodes[node0] ^ nodes[node1]:
            result = 1
        else:
            result = 0
    else:
        raise Exception("Unknown gate: " + gate)

    nodes[cur] = result
    return nodes[cur]

def solution_1(nodes, ngc):
    q = collections.deque([n for n in nodes.keys()])
    edges = collections.defaultdict(set)
    in_degrees = collections.defaultdict(set)
    for n2, (n0, g, n1) in ngc.items():
        in_degrees[n2].add(n0)
        in_degrees[n2].add(n1)
        edges[n0].add(n2)
        edges[n1].add(n2)

    while q:
        cur = q.popleft()

        solve(cur, nodes, ngc)
        for nei in edges[cur]:
            in_degrees[nei].remove(cur)
            if len(in_degrees[nei]) == 0:
                q.append(nei)

    zs = [ n for n in nodes.keys() if n[0] == 'z' ]
    zs.sort(reverse=True)
    bits = ''.join([ str(nodes[n]) for n in zs ])
    return int(bits, 2)

def parse_input2(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        nodes = dict()
        in_degrees = collections.defaultdict(set)
        nodes_and_gates = dict()
        edges = collections.defaultdict(set)

        data = f.read().strip()
        inits, gates = data.split('\n\n')
        inits = inits.split('\n')
        gates = gates.split('\n')

        for gate in gates:
            node0, gate, node1, arrow, node2 = gate.split(' ')
            nodes_and_gates[node2] = (node0, gate, node1)
            in_degrees[node2].add(node0)
            in_degrees[node2].add(node1)
            edges[node0].add(node2)
            edges[node1].add(node2)

        q = collections.deque()
        for init in inits:
            node, val = init.split(': ')
            nodes[node] = int(val)
            q.append(node)

    xs = [ n for n in nodes.keys() if n[0] == 'x' ]
    xs.sort(reverse=True)
    bits = ''.join([ str(nodes[n]) for n in xs ])
    x = int(bits, 2)

    ys = [ n for n in nodes.keys() if n[0] == 'y' ]
    ys.sort(reverse=True)
    bits = ''.join([ str(nodes[n]) for n in ys ])
    y = int(bits, 2)

    z_target = x + y
    return nodes, nodes_and_gates, in_degrees, edges, q, z_target

def solution_2(nodes, nodes_and_gates, z_target):
    q = collections.deque([n for n in nodes.values()])
    edges = collections.defaultdict(set)
    in_degrees = collections.defaultdict(set)
    for n2, (n0, g, n1) in nodes_and_gates.items():
        in_degrees[n2].add(n0)
        in_degrees[n2].add(n1)
        edges[n0].add(n2)
        edges[n1].add(n2)

    while q:
        cur = q.popleft()

        solve(cur, nodes, nodes_and_gates)
        for nei in edges[cur]:
            in_degrees[nei].remove(cur)
            if len(in_degrees[nei]) == 0:
                q.append(nei)

    zs = [ n for n in nodes.keys() if n[0] == 'z' ]
    zs.sort(reverse=True)
    bits = ''.join([ str(nodes[n]) for n in zs ])
    return int(bits, 2) == z_target

if __name__ == "__main__":
    start = timer()
    nodes, nodes_and_gates, in_degrees, edges, q = parse_input("puzzle_input/d24_input.txt")
    result = solution_1(nodes, nodes_and_gates, in_degrees, edges, q )
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')

    # print()
    # start = timer()
    # edges = parse_input("puzzle_input/d23_input.txt")
    # best = solution_2(edges)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution2: {best}')
    #
