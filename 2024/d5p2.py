from timeit import default_timer as timer
import collections

def read_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        rules = collections.defaultdict(set)
        inverse_rules = collections.defaultdict(set)
        updates = []
        update_section = False
        for line in f:
            if line == '\n':
                update_section = True
                continue

            s = line[:-1]
            if not update_section:
                s = s.split("|")
                l, r = int(s[0]), int(s[1])
                rules[l].add(r)
                inverse_rules[r].add(l)
            else:
                s = s.split(",")
                updates.append([int(page) for page in s])

    # for r in rules:
    #     print(r, end=" ")
    #     print(rules[r])
    # print()
    # for ir in inverse_rules:
    #     print(ir, end=" ")
    #     print(inverse_rules[ir])
    # print()
    # for u in updates:
    #     print(u)


    return rules, inverse_rules, updates

def is_valid(rules, update):
    for i, l in enumerate(update):
        for r in update[i+1:]:
            if r not in rules[l]:
                return False
    return True

def reorder(rules, inverse_rules, pages):
    reordered_update = []
    useful_inverse = collections.defaultdict(set)
    for p in pages:
        for neighbor in inverse_rules[p]:
            if neighbor in pages:
                useful_inverse[p].add(neighbor)
    useful_rules = collections.defaultdict(set)
    for p in pages:
        for neighbor in rules[p]:
            if neighbor in pages:
                useful_rules[p].add(neighbor)


    stack = [ p for p in pages if len(useful_inverse[p]) == 0 ]
    while stack:
        p = stack.pop()
        reordered_update.append(p)
        for nei in useful_rules[p]:
            useful_inverse[nei].remove(p)
            if len(useful_inverse[nei]) == 0:
                stack.append(nei)

    return reordered_update


def solution(rules, inverse_rules, update):
    total = 0
    for update in updates:
        if not is_valid(rules, update):
            reordered_update = reorder(rules, inverse_rules, set(update))
            l, r = 0, len(reordered_update) - 1
            m = (r - l) // 2 + l
            total += reordered_update[m]

    return total

filename = "2024//d5p1_input_ex.txt"
rules, inverse_rules, updates = read_input(filename)
result = solution(rules, inverse_rules, updates)
print(result)
assert result == 123

start = timer()
filename = "2024//d5p1_input.txt"
rules, inverse_rules, updates = read_input(filename)
result = solution(rules, inverse_rules, updates)
print(result)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result)
