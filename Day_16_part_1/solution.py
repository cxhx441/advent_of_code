from collections import deque

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

def get_travel_times_from_node(graph, valve):
    travel_times = dict()
    visited = set()
    cost = 0
    q = deque()
    q.appendleft((cost, valve))
    while q:
        cost, cur_valve = q.pop()
        visited.add(cur_valve)
        travel_times[cur_valve] = cost
        for neighbor in graph[cur_valve]:
            if neighbor not in visited:
                q.appendleft((cost+1, neighbor))
    return travel_times

infile = "sample_input.txt"
infile = "real_input.txt"
graph = create_graph(infile)
start = [x for x in graph.keys()][0]
useful_valves = [x for x in graph.keys() if x.flow_rate != 0 or x == start]

travel_times = dict()
for valve in useful_valves:
    travel_times[valve] = get_travel_times_from_node(graph, valve)

print(useful_valves)
print()
for i in graph:
    print(i, graph[i])
print()
for i in travel_times:
    print(i, travel_times[i])
print()
for i in useful_valves:
    print(i, i.flow_rate)

# do a backtracking thing
def backtracking(start, travel_times, useful_valves, mins=30):
    def helper(cur_valve, mins, cur_max, index, choices):
        if mins < 0:
            return
        if mins == 0:
            solutions.append(cur_max)
        next_valve = useful_valves[index]
        mins -= travel_times[cur_valve][next_valve]
        choices.append(next_valve)
        mins -= 1
        cur_max += mins*next_valve.flow_rate
        index += 1
        helper(next_valve,
                mins,
                cur_max,
                index,
                choices)
        index -= 1
        cur_max -= mins*next_valve.flow_rate
        mins += 1
        choices.pop()
        mins += travel_times[cur_valve][next_valve]
        return

    solutions = []
    choices = []
    helper(start, mins, 0, 1, choices)
    return solutions
# Python function to print permutations of a given list
# solution = backtracking(start, travel_times, useful_valves, mins=30)
