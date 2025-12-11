# import collections
import time
import copy

# fname = "2025/puzzle_input/d11p2_example.txt"
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

def get_reachable(start, end):
    stack = [start]
    seen = set()
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        if cur  == end:
            continue
        stack += edge_map[cur]
    return seen


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
    for node in all_nodes:
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


def svr_to_out_with_fft_and_dac_DFS():
    #  svr > fft (no dac) = 1
    #  svr > dac (no fft) = 1
    #  fft > dac          = 1
    #  dac > fft          = 0
    svr_fft_nodac = dfs("svr", "fft", "dac")
    svr_dac_nofft = dfs("svr", "dac", "fft")
    fft_dac = dfs("fft", "dac")
    dac_fft = dfs("dac", "fft")

    #  fft > out          = 4
    #  dac > out          = 2
    fft_out = dfs("fft", "out")
    dac_out = dfs("dac", "out")
    print("done")

    # svr > dac (with fft) = 1
        # svr > fft (no dac) * fft > dac = 1 * 1
    svr_dac_w_fft = svr_fft_nodac * fft_dac

    # svr > fft (with dac) = 0
        # svr > dac (no fft) * dac > fft = 1 * 0
    svr_fft_w_dac = svr_dac_nofft * dac_fft

    # fft > out (with dac) = 0
        # fft > out * svr > fft (with_dac) = 4 * 0
    fft_out_w_dac = fft_out * svr_fft_w_dac

    # dac > out (with fft) = 2
        # dac > out * svr > dac (with_fft) = 2 * 1
    dac_out_w_fft = dac_out * svr_dac_w_fft

    # result = fft > out (with dac) + dac > out (with fft) = 2 + 0
    result = fft_out_w_dac + dac_out_w_fft
    return result

def svr_to_out_with_fft_and_dac():
    #  svr > fft (no dac) = 1
    #  svr > dac (no fft) = 1
    #  fft > dac          = 1
    #  dac > fft          = 0
    svr_fft_nodac = get_ways_to_reach("svr", "fft", "dac")
    svr_dac_nofft = get_ways_to_reach("svr", "dac", "fft")
    fft_dac = get_ways_to_reach("fft", "dac")
    dac_fft = get_ways_to_reach("dac", "fft")

    #  fft > out          = 4
    #  dac > out          = 2
    fft_out = get_ways_to_reach("fft", "out")
    dac_out = get_ways_to_reach("dac", "out")
    print("done")

    # svr > dac (with fft) = 1
        # svr > fft (no dac) * fft > dac = 1 * 1
    svr_dac_w_fft = svr_fft_nodac * fft_dac

    # svr > fft (with dac) = 0
        # svr > dac (no fft) * dac > fft = 1 * 0
    svr_fft_w_dac = svr_dac_nofft * dac_fft

    # fft > out (with dac) = 0
        # fft > out * svr > fft (with_dac) = 4 * 0
    fft_out_w_dac = fft_out * svr_fft_w_dac

    # dac > out (with fft) = 2
        # dac > out * svr > dac (with_fft) = 2 * 1
    dac_out_w_fft = dac_out * svr_dac_w_fft

    # result = fft > out (with dac) + dac > out (with fft) = 2 + 0
    result = fft_out_w_dac + dac_out_w_fft
    return result

if "example" in fname:
    print("\nways_to_reach: EXAMPLE")
    start_time = time.perf_counter()
    print(f" == 2 {svr_to_out_with_fft_and_dac() == 2}")
    end_time = time.perf_counter()
    print(f"execution time: {(end_time - start_time):.6f}")
else:
    print("\nways_to_reach: REAL")
    start_time = time.perf_counter()
    print(f" == 2 {svr_to_out_with_fft_and_dac() == 2}")
    end_time = time.perf_counter()
    print(f"execution time: {(end_time - start_time):.6f}")
    print(svr_to_out_with_fft_and_dac())
