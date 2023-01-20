from functools import cmp_to_key
data = [
[1,1,3,1,1],
[1,1,5,1,1],

[[1],[2,3,4]],
[[1],4],

[9],
[[8,7,6]],

[[4,4],4,4],
[[4,4],4,4,4],

[7,7,7,7],
[7,7,7],

[],
[3],

[[[]]],
[[]],

[1,[2,[3,[4,[5,6,7]]]],8,9],
[1,[2,[3,[4,[5,6,0]]]],8,9],
]
IN_ORDER = "IN_ORDER"
OUT_OF_ORDER = "OUT_OF_ORDER"
TBD = "TBD"
def in_right_order(first, second):
    if type(first) == int and type(second) == int:
        if first < second: return IN_ORDER
        elif first > second: return OUT_OF_ORDER
        else: return TBD
    elif type(first) == int and type(second) == list:
        first = [first]
    elif type(first) == list and type(second) == int:
        second = [second]

    #type(first) == list and type(second) == list:
    i = j = 0
    while True:
        if i >= len(first) and j >= len(second): return TBD # finish same time
        elif i >= len(first): return IN_ORDER # first ran out of items
        elif j >= len(second): return OUT_OF_ORDER # second ran out of items

        query = in_right_order(first[i], second[j])
        if query in (IN_ORDER, OUT_OF_ORDER):
            return query
        elif query == TBD:
            i += 1
            j += 1

    # turn into lists

pairs = []
for i in range(0, len(data), 2):
    first = data[i]
    second = data[i+1]
    pairs.append((first, second))

pairs.insert(0, None)
cur_sum = 0
for i in range(1, len(pairs)):
    first, second = pairs[i]
    if in_right_order(first, second) == IN_ORDER:
        cur_sum += i

print(cur_sum)

def comparer(first, second):
    if in_right_order(first, second) == IN_ORDER:
        return 1
    elif in_right_order(first, second) == OUT_OF_ORDER:
        return -1
    else:
        return 0
inner_two = [2]
inner_six = [6]
two = [inner_two]
six = [inner_six]
data.append(two)
data.append(six)
data.sort(key=cmp_to_key(comparer), reverse=True)
print(data)
data.insert(0, None)
for i in range(1, len(data)):
    if len(data[i]) == 1 and type(data[i]) == list and data[i][0] == inner_two:
        two = i
    if len(data[i]) == 1 and type(data[i]) == list and data[i][0] == inner_six:
        six = i

print(two*six)

