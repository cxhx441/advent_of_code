def input_to_list(infile):
    data = []
    with open(infile, 'r') as f:
        for line in f:
            elf1, elf2 = line[:-1].split(',')
            ranges = elf1.split('-') + elf2.split('-')
            data.append([int(x) for x in ranges])
    return data

data = input_to_list("real_input.txt") #

cur_sum = 0
for item in data:
    elf1_range = range(item[0], item[1]+1)
    elf2_range = range(item[2], item[3]+1)
    union = set(elf1_range) | set(elf2_range)
    intersection = set(elf1_range) & set(elf2_range)
    if union == set(elf1_range) or union == set(elf2_range) or intersection != set():
        cur_sum += 1
print(cur_sum)
