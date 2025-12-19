from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

# must visit each location exactly once.
# find shortest path.
# Shortest Hamiltonian Path (touch each node exactly once) Problem similar
#   to traveling salesman

# ... check all posssible paths?

def parse_pt1(fname):
    adj_map = defaultdict(list)
    nodes = set()
    print()
    with open(fname, 'r', encoding="UTF-8") as f:
        for line in f:
            cities, weight = line[:-1].split(" = ")
            a, b = cities.split(" to ")
            adj_map[a].append((b, int(weight)))
            adj_map[b].append((a, int(weight)))
            nodes.add(a)
            nodes.add(b)
            # adj_map[a].append(b)
    return adj_map, nodes

def networkx_draw(adj):
    G = nx.Graph()
    for a, val in adj.items():
        G.add_node(a)
        for b, weight in val:
            G.add_edge(a, b, weight=weight)
    print(list(G))

    # Thanks Gemini.
    # It is important to use the same 'pos' for all drawing components
    pos = nx.spring_layout(G)

    # 5. Draw the graph components
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

    # 6. Get the edge weights and format them into a dictionary for labels
    edge_weights = nx.get_edge_attributes(G, 'weight')
    # The dictionary is keyed by (u, v) and the value is the label to draw
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights, font_color='red')
    # edge_weights = nx.get_edge_attributes(G, 'weight')
    # nx.draw(G, with_labels=True, font_color="black", edge_labels=edge_weights)
    plt.show()

def backtrack(node, cost, unseen, results):
    if len(unseen) == 0:
        results.append(cost)
        return

    for nei, weight in adj[node]:
        if nei in unseen:
            unseen.remove(nei)
            backtrack(nei, cost + weight, unseen, results)
            unseen.add(nei)

# adj, nodes = parse_pt1("2015/puzzle_input/d9_ex.txt")
adj, nodes = parse_pt1("2015/puzzle_input/d9.txt")
results = []
unseen = nodes.copy()
for node in nodes:
    unseen.remove(node)
    backtrack(node, 0, unseen, results)
    unseen.add(node)
print(results)
print(sorted(results))
print(min(results)) # part 1
print(max(results)) # part 2
networkx_draw(adj)
