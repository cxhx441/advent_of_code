from timeit import default_timer as timer
import collections
import re
import itertools

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        data = f.read().strip()
        edges = collections.defaultdict(set)
        pattern = r'(\w+)-(\w+)'
        matches = re.findall(pattern, data)
        for a, b in matches:
            edges[a].add(b)
            edges[b].add(a)

    return edges



def solution_1(edges):
    groups = set()
    for n, e in edges.items():
        combos2 = list(itertools.combinations(e, 2))
        for c2 in combos2:
            if c2[0] in edges[c2[1]]:
                if 't' in (n[0], c2[0][0], c2[1][0]):
                    group = [n, *c2]
                    group.sort()
                    group = tuple(group)
                    groups.add(group)
    return groups


def solution_2(edges):
    def nodes_are_connected(combo):
        for cur0 in combo:
            for cur1 in combo:
                if cur0 == cur1:
                    continue
                if cur0 not in edges[cur1]:
                    return False
        return True

    groups = set()
    seen = set()
    for n, e in edges.items():
        if n in seen:
            continue
        for i in range(2, len(e)):
            combos = list(itertools.combinations(e, i))
            for combo in combos:
                # check that each node is connected to the other
                if nodes_are_connected(combo):
                    seen.add(n)
                    for c in combo:
                        seen.add(c)
                    group = list(combo) + [n]
                    group.sort()
                    group = tuple(group)
                    groups.add(group)

    best = set()
    for group in groups:
        if len(group) > len(best):
            best = group
    print(','.join(best))
    return set(best)


if __name__ == "__main__":
    start = timer()
    edges = parse_input("puzzle_input/d23_input.txt")
    tees = solution_1(edges)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {len(tees)}')

    print()
    start = timer()
    edges = parse_input("puzzle_input/d23_input.txt")
    best = solution_2(edges)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution2: {best}')

