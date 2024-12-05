from timeit import default_timer as timer
import collections

def read_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        rules = collections.defaultdict(set)
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
            else:
                s = s.split(",")
                updates.append([int(page) for page in s])

    # for r in rules:
    #     print(r, end=" ")
    #     print(rules[r])
    # print()
    # for u in updates:
    #     print(u)

    return rules, updates

def is_valid(rules, update):
    for i, l in enumerate(update):
        for r in update[i+1:]:
            if r not in rules[l]:
                return False
    return True

def solution(rules, updates):
    total = 0
    for update in updates:
        if is_valid(rules, update):
            l, r = 0, len(update) - 1
            m = (r - l) // 2 + l
            total += update[m]

    return total

filename = "2024//d5p1_input_ex.txt"
rules, updates = read_input(filename)
result = solution(rules, updates)
print(result)
assert result == 143

start = timer()
filename = "2024//d5p1_input.txt"
rules, updates = read_input(filename)
result = solution(rules, updates)
print(result)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result)
