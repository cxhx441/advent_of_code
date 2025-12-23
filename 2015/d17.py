from itertools import chain, combinations

LITERS = 150
jugs = [ 50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40 ]
# LITERS = 25
# jugs = [ 20, 15, 10, 5, 5 ]


def fits(jug_combo, need):
    for j in jug_combo:
        need -= j
        if need < 0:
            return False
    return need == 0

# def powerset(iterable):
#     result = [[]]
#     for x in iterable:
#         new = []
#         for r in result:
#             rc = r + [x]
#             new.append(rc)
#         result += new
#     return result

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(iterable) + 1 ) )

# p1
count = 0
for p in powerset(jugs):
    if fits(p, LITERS):
        count += 1
print(count)

minimum = float("inf")
for p in powerset(jugs):
    if len(p) < minimum and fits(p, LITERS):
        minimum = len(p)

count = 0
for p in powerset(jugs):
    if len(p) == minimum and fits(p, LITERS):
        count += 1
print(count)
