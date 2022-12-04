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
rucksacks = input_to_list("real_input.txt") #

cur_sum = 0
for i in range(0, len(rucksacks), 3):
    rucksack_1 = set(rucksacks[i])
    rucksack_2 = set(rucksacks[i+1])
    rucksack_3 = set(rucksacks[i+2])

    badge_set = rucksack_1 & rucksack_2 & rucksack_3 # intersection
    cur_sum += priority(badge_set.pop())

print(cur_sum)
