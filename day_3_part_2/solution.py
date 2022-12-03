def input_to_list(infile):
    data = []
    with open(infile, 'r') as f:
        for line in f:
            data.append(line[:-1])
    return data

def priority(character):
    if ord(character) in range(97, 123):
        return ord(character) - 96
    else:
        return ord(character) - 64 + 26

# items = input_to_list("sample_input.txt") #
items = input_to_list("real_input.txt") #

print(items)
cur_sum = 0
for i in range(0, len(items), 3):
    line1 = set(items[i])
    line2 = set(items[i+1])
    line3 = set(items[i+2])

    badge = line1.intersection(line2.intersection(line3))
    for k in badge:
        badge = k
    cur_sum += priority(badge)



print(cur_sum)
