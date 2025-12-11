import collections
import time
import copy

fname = "2025/puzzle_input/d11p1_example.txt"
fname = "2025/puzzle_input/d11p1_input.txt"

def read():
    edge_map = dict()
    all_nodes = set()
    reverse_map = dict()
    with open(fname, 'r', encoding="UTF-8") as f:
        for line in f:
            a, b_list = line[:-1].split(': ')
            b_list = b_list.split(' ')
            edge_map[a] = b_list

            for node in edge_map[a]:
                if node not in reverse_map:
                    reverse_map[node] = []
                reverse_map[node].append(a)
            all_nodes = all_nodes | set(b_list)
            all_nodes.add(a)
            for node in all_nodes:
                if node not in reverse_map:
                    reverse_map[node] = []
    return edge_map, reverse_map, all_nodes

edge_map, reverse_map, all_nodes = read()

def dfs(start, target, exclude=None):
    stack = [start]
    count = 0
    while stack:
        cur = stack.pop()
        if cur == exclude:
            continue
        if cur == target:
            count += 1
            continue
        if cur in edge_map:
            stack += edge_map[cur]
    return count

def bfs(start, target, exclude=None):
    q = collections.deque([start])
    count = 0
    while q:
        lq = len(q)
        for _ in range(lq):
            cur = q.popleft()
            if cur == exclude:
                continue
            if cur == target:
                count += 1
                continue
            if cur in edge_map:
                for node in edge_map[cur]:
                    q.append(node)
    return count

def get_ways_to_reach(start, target, exclude=None):
    edge_map_cpy = copy.deepcopy(edge_map)
    reverse_map_cpy = copy.deepcopy(reverse_map)
    all_nodes_cpy = all_nodes.copy()
    if exclude is not None:
        all_nodes_cpy.remove(exclude)
        del edge_map_cpy[exclude]
        for val in reverse_map_cpy.values():
            if exclude in val:
                val.remove(exclude)

    ways_to_reach = { key : None for key in edge_map_cpy.keys()}
    for node in all_nodes_cpy:
        if node not in ways_to_reach:
            ways_to_reach[node] = 0
        # if reverse_map[node] == []:
        #     ways_to_reach[node] = 0

    ways_to_reach[start] = 1
    stack = [target]
    while stack:
        cur = stack.pop()
        reach_counts = [ ways_to_reach[key] for key in reverse_map_cpy[cur] ]
        if None in reach_counts:
            stack.append(cur)
            stack += [key for key in reverse_map_cpy[cur]]
        else:
            if cur == start:
                continue
            ways_to_reach[cur] = sum(reach_counts)
    return ways_to_reach[target]

def dfs_old(start, target, exclude=None):
    stack = [start]
    count = 0
    while stack:
        cur = stack.pop()
        if cur == exclude:
            continue
        if cur == target:
            count += 1
            continue
        if cur in edge_map:
            stack += edge_map[cur]
    return count

if "example" in fname:
    print("dfs: EXAMPLE")
    print(f" == 5 {dfs("you", "out") == 5}")
    print(f" == 3 {dfs("you", "out", "eee") == 3}")
    print(f" == 2 {dfs("you", "out", "ccc") == 2}")
    print(f" == 3 {dfs("you", "out", "bbb") == 3}")

    print("\nbfs")
    print(f" == 5 {bfs("you", "out") == 5}")

    print("\nways_to_reach")
    print(f" == 3 {get_ways_to_reach("you", "out", "eee") == 3}")
    print(f" == 2 {get_ways_to_reach("you", "out", "ccc") == 2}")
    print(f" == 3 {get_ways_to_reach("you", "out", "bbb") == 3}")
    print(f" == 5 {get_ways_to_reach("you", "out") == 5}")
else:
    print("dfs: REAL")
    start_time = time.perf_counter()
    print(f" == 696 {dfs("you", "out") == 696}")
    end_time = time.perf_counter()
    print(f"execution time: {(end_time - start_time):.6f}")

    print("\nbfs")
    start_time = time.perf_counter()
    print(f" == 696 {bfs("you", "out") == 696}")
    end_time = time.perf_counter()
    print(f"execution time: {(end_time - start_time):.6f}")

    print("\nways_to_reach")
    start_time = time.perf_counter()
    print(f" == 696 {get_ways_to_reach("you", "out") == 696}")
    end_time = time.perf_counter()
    print(f"execution time: {(end_time - start_time):.6f}")
    print(get_ways_to_reach("svr", "out"))

