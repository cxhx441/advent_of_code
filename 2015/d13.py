from itertools import permutations

FNAME = "2015/puzzle_input/d13.txt"
# FNAME = "2015/puzzle_input/d13ex.txt";

mp = dict()
people = set()
with open(FNAME, "r", encoding="UTF-8") as f:
    for line in f:
        line = line[:-2].split(" ")
        source, sign, amount, receiver = line[0], line[2], int(line[3]), line[-1]
        if sign == "lose":
            amount *= -1
        mp[(source, receiver)] = amount
        people.add(source)

me = "Craig"
for person in people:
    mp[(me, person)] = 0
    mp[(person, me)] = 0
people.add(me)

best_result = 0
for perm in permutations(people):
    result = 0
    for i in range(len(people)):
        left = mp[perm[i], perm[i - 1]]
        right = mp[perm[i], perm[(i + 1) % len(people)]]
        result += left + right
    best_result = max(best_result, result)
print(best_result)
