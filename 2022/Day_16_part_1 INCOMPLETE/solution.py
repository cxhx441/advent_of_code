from collections import deque
from itertools import permutations

class valve():
    def __init__(self, label, flow_rate):
        self.label = label
        self.flow_rate = flow_rate
    def __lt__(self, other):
        return self.flow_rate < other.flow_rate

    def __repr__(self) -> str:
        return self.label

def create_graph(infile):
    with open(infile, 'r') as f:
        graph = dict()
        valves = dict()
        for line in f:
            valve_label = line[6:8]
            valve_flow_rate = int(line[line.index('=')+1:line.index(';')])
            valves[valve_label] = valve(valve_label, valve_flow_rate)

        f.seek(0)
        for line in f:
            valve_label = line[6:8]
            if 'valves ' in line:
                connected_index = line.index('valves ')+7
            else:
                connected_index = line.index('valve ')+6
            connected_valves = line[connected_index:-1]
            connected_valves = connected_valves.split(',')
            graph[valves[valve_label]] = [valves[x.strip(' ')] for x in connected_valves]
    return graph

def get_useful_travel_plus_open_times_from_node(graph, valve, valves_of_interest):
    travel_times = dict()
    visited = set()
    cost = 0
    q = deque()
    q.appendleft((cost, valve))
    while q:
        cost, cur_valve = q.pop()
        visited.add(cur_valve)
        # if cur_valve in valves_of_interest and cur_valve != valve:
        if cur_valve in valves_of_interest:
             travel_times[cur_valve] = cost + 1 # plus one to open it
        # travel_times[cur_valve] = cost
        for neighbor in graph[cur_valve]:
            if neighbor not in visited:
                q.appendleft((cost+1, neighbor))
    return travel_times

def get_score(valve_path):
    flow = 0
    for choice in valve_path:
        valve, time_remaining = choice
        flow += valve.flow_rate*time_remaining
    return flow

def crct_get_score(valve_path):
    flow = 0
    for valve, time_remaining in valve_path.items():
        flow += valve.flow_rate*time_remaining
    return flow

infile = "sample_input.txt"
infile = "real_input.txt"
graph = create_graph(infile)
start = [x for x in graph.keys()][0]
useful_valves = [x for x in graph.keys() if x.flow_rate != 0]

useful_travel_times = dict()
for valve in [start]+useful_valves:
    useful_travel_times[valve] = get_useful_travel_plus_open_times_from_node(graph, valve, useful_valves)

print('useful_valves')
print(useful_valves)
print()
print('graph')
for i in graph:
    print(i, graph[i])
print()
print('travel_times')
for i in useful_travel_times:
    print(i, useful_travel_times[i])
print()
print()
print('flow_rates')
for i in useful_valves:
    print(i, i.flow_rate)

def crct_get_permutations(useful_travel_times, useful_valves, cur_valve, time_left, choices={}):
    results = [choices]
    if time_left < 2:
        return results
    for nxt_valve in useful_valves:
        new_time_left = time_left - useful_travel_times[cur_valve][nxt_valve]
        new_choices = choices | {nxt_valve : new_time_left}
        new_useful_valves = useful_valves - {nxt_valve}
        results += (crct_get_permutations(useful_travel_times, new_useful_valves, nxt_valve, new_time_left, new_choices))
    return results

def get_permutations(useful_travel_times, useful_valves, start, time_left):
    def helper(valves, cur_valve, time_left, choices):
        # print(choices)
        if time_left >= 0:
            results.append(choices.copy())
        if time_left < 2:
            return
        for nxt_valve in valves:

            time_left -= useful_travel_times[cur_valve][nxt_valve]
            choices.append((nxt_valve, time_left))

            valves.remove(nxt_valve)
            helper(valves, nxt_valve, time_left, choices)
            valves.add(nxt_valve)

            choices.pop()
            time_left += useful_travel_times[cur_valve][nxt_valve]

    results = []
    choices = []
    helper(set(useful_valves), start, time_left, choices)
    return results


crct_perms = crct_get_permutations(useful_travel_times, set(useful_valves), start, 30)
perms = get_permutations(useful_travel_times, useful_valves, start, 30)
print('')
print('hi')
for p in perms:
    print(p)
print(len(perms))

# for p in crct_perms:
#     print(p)
print(len(crct_perms))

max_score = 0
for p in crct_perms:
    max_score = max(crct_get_score(p), max_score)
print(max_score)

max_score = 0
for p in perms:
    print(get_score(p), p)
    if get_score(p) >= max_score:
        max_score = get_score(p)
        good = p
print(max_score, good)


print('travel_times')
for i in useful_travel_times:
    print(i, useful_travel_times[i])
print()
