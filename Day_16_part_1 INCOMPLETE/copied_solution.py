import numpy as np
import re
from queue import PriorityQueue

def heuristic(node, time_remaining, visited, flow_rates, closest_distance):
    max_score = 0
    scores = []
    nodes = []
    for node, distance in closest_distance[node].items():
        if node in visited:
            continue
        if distance < time_remaining:
            score = (time_remaining - distance - 1) * flow_rates[node]
            if score > 0:
                scores.append(score)
                nodes.append(node)
                max_score += score
    sort_args = np.argsort(scores)[::-1]
    scores = [scores[x] for x in sort_args]
    ordered_nodes = [nodes[x] for x in sort_args]
    return max_score, scores, ordered_nodes

def best_score(min_score, time_remaining, node, visited, neighbors, flow_rates, closest_distance):
    max_score, ordered_weights, ordered_nodes = heuristic(node, time_remaining, visited, flow_rates, closest_distance)
    if max_score <= min_score:
        return 0
    actual_max_score = min_score
    for weight, n in zip(ordered_weights, ordered_nodes):
        visited.add(n)
        score = weight + best_score(
            max(actual_max_score - weight, 0),
            time_remaining - closest_distance[node][n] - 1,
            n,
            visited,
            neighbors,
            flow_rates,
            closest_distance
        )
        actual_max_score = max(actual_max_score, score)
        visited.remove(n)
    return actual_max_score

def distance(start, end, neighbors):
    queue = PriorityQueue()
    queue.put((0, start))

    visited = set()
    visited.add(start)

    while not queue.empty():
        distance, location = queue.get()
        if location == end:
            return distance
        for neighbor in neighbors[location]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((distance + 1, neighbor))
    return 0



## Code execution

pattern = r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.*)"

neighbors = {}
flow_rates = {}

with open("real_input.txt", 'r') as f:
    input_string = f.read()
    input_lines = input_string.split('\n')

    for i in range(len(input_lines)-1):
        line = input_lines[i]

        matched = re.findall(pattern, line)
        print(matched)
        flow_rate = int(matched[0][1])
        valve = matched[0][0]
        to = matched[0][2].split(', ')
        neighbors[valve] = neighbors.get(valve, set(to))
        flow_rates[valve] = flow_rate

nodes = list(neighbors.keys())

closest_distance = {}
for m in nodes:
    for n in nodes:
        if m == n:
            continue
        closest_distance[m] = closest_distance.get(m, {})
        closest_distance[m][n] = distance(m, n, neighbors)

answer = best_score(0, 30, 'AA', set(), neighbors, flow_rates, closest_distance)
print(answer)
