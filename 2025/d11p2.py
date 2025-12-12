import collections
import time
import copy

# fname = "2025/puzzle_input/d11p2_example.txt"
fname = "2025/puzzle_input/d11p1_input.txt"
def read():
    adj_list = collections.defaultdict(list)
    all_nodes = set()
    reverse_adj = collections.defaultdict(list)
    with open(fname, 'r', encoding="UTF-8") as f:
        for line in f:
            a, b_list = line[:-1].split(': ')
            b_list = b_list.split(' ')
            adj_list[a] = b_list

            for node in adj_list[a]:
                if node not in reverse_adj:
                    reverse_adj[node] = []
                reverse_adj[node].append(a)
            all_nodes = all_nodes | set(b_list)
            all_nodes.add(a)
            for node in all_nodes:
                if node not in reverse_adj:
                    reverse_adj[node] = []
    return adj_list, reverse_adj, all_nodes

adj_list, reverse_adj, all_nodes = read()

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
        stack += adj_list[cur]
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
        if cur in adj_list:
            stack += adj_list[cur]
    return count

def get_ways_to_reach(start, target, exclude=None):
    adj_list_cp = copy.deepcopy(adj_list)
    reverse_adj_cp = copy.deepcopy(reverse_adj)
    all_nodes_cpy = all_nodes.copy()
    if exclude is not None:
        all_nodes_cpy.remove(exclude)
        del adj_list_cp[exclude]
        for val in reverse_adj_cp.values():
            if exclude in val:
                val.remove(exclude)

    ways_to_reach = { key : None for key in adj_list_cp.keys()}
    for node in all_nodes:
        if node not in ways_to_reach:
            ways_to_reach[node] = 0
        # if reverse_adj[node] == []:
        #     ways_to_reach[node] = 0

    ways_to_reach[start] = 1
    stack = [target]
    while stack:
        cur = stack.pop()
        reach_counts = [ ways_to_reach[key] for key in reverse_adj_cp[cur] ]
        if None in reach_counts:
            stack.append(cur)
            stack += [key for key in reverse_adj_cp[cur]]
        else:
            if cur == start:
                continue
            ways_to_reach[cur] = sum(reach_counts)
    return ways_to_reach[target]

def paths(start, target):
    npaths = { node : None for node in reverse_adj }
    npaths[start] = 1
    stack = [target]
    while stack:
        cur = stack.pop()
        if npaths[cur] is not None:
            continue

        preds = reverse_adj[cur]
        unresolved = [ p for p in preds if npaths[p] is None ]
        if unresolved:
            stack.append(cur)
            stack.extend(unresolved)
        else:
            npaths[cur] = sum(npaths[p] for p in preds)
    return npaths[target]

def solve():
    return paths("svr", "fft") * paths("fft", "dac") * paths("dac", "out")

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

def kahns_topo():
    adj = adj_list
    indeg = {u: 0 for u in all_nodes}
    for u in adj:
        for v in adj[u]:
            indeg[v] += 1

    q = collections.deque([u for u in adj if indeg[u] == 0])
    count = 0

    while q:
        u = q.popleft()
        count += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return count != len(adj)

# def cycles_present():

#     for start in adj_list:
#         if start in visited:
#             continue

#         stack = [(start, iter(adj_list[str]))]

#         stack = [u]
#         in_stack.add(u)
#         while stack:
#             cur = stack.pop()
#             if cur in in_stack:
#                 return True
#             in_stack.remove(cur)

#             if cur in seen:
#                 return False

#             for v in adj_list[u]:
#                 in_stack.add(v)
#                 stack.append(v)

#     return False


if "example" in fname:
    print("\nways_to_reach: EXAMPLE")
    start_time = time.perf_counter()
    print(f" == 2 {svr_to_out_with_fft_and_dac() == 2}")
    end_time = time.perf_counter()
    print(f"execution time: {(end_time - start_time):.6f}")
else:
    print("\nways_to_reach: REAL")
    start_time = time.perf_counter()
    print(f" == 473741288064360 {svr_to_out_with_fft_and_dac() == 473741288064360}")
    end_time = time.perf_counter()
    print(f"execution time: {(end_time - start_time):.6f}")

    print("\nways_to_reach: REAL")
    start_time = time.perf_counter()
    print(f" == 473741288064360 {solve() == 473741288064360}")
    end_time = time.perf_counter()
    print(f"execution time: {(end_time - start_time):.6f}")

print(kahns_topo())
