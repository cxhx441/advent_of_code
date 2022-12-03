def input_to_list(infile):
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line[:-1]
            halfway = len(line)//2
            comp1 = set(line[:halfway])
            comp2 = set(line[halfway:])
            item = comp1.intersection(comp2)
            data.append(item)
    return data

def priority(character):
    if ord(character) in range(97, 123):
        return ord(character) - 96
    else:
        return ord(character) - 64 + 26

# items = input_to_list("sample_input.txt") #
items = input_to_list("real_input.txt") #

# print(items)
cur_sum = 0
for item in items:
    for i in item:
        cur_sum += priority(i)
print(cur_sum)
