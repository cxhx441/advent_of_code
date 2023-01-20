def input_to_list(infile):
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line[:-1]
            halfway = len(line)//2
            compartment_1 = set(line[:halfway])
            compartment_2 = set(line[halfway:])
            item = compartment_1 & compartment_2 # intesersection
            data.append(item)
    return data

def priority(character):
    if ord(character) in range(97, 123):
        return ord(character) - 96
    else:
        return ord(character) - 64 + 26

# items = input_to_list("sample_input.txt") #
common_items = input_to_list("real_input.txt") #

cur_sum = 0
for item in common_items:
    cur_sum += priority(item.pop())

print(cur_sum)
