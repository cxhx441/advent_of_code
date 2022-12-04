def input_to_list(infile):
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line[:-1]
            elf1, elf2 = line.split(',')
            elf1_lower, elf1_upper = elf1.split('-')
            elf2_lower, elf2_upper = elf2.split('-')
            # elf1_range = int(elf1_lower), int(elf1_upper)
            # elf2_range = int(elf2_lower), int(elf2_upper)
            # data.append((elf1_range, elf2_range))
            data.append((int(elf1_lower), int(elf1_upper), int(elf2_lower), int(elf2_upper)))
    return data
data = input_to_list("sample_input.txt") #
data = input_to_list("real_input.txt") #
print(data)

cur_sum = 0
for item in data:
    elf1_range = range(item[0], item[1]+1)
    elf2_range = range(item[2], item[3]+1)
    unioned = set(elf1_range) | set(elf2_range)
    intersection = set(elf1_range) & set(elf2_range)
    if unioned == set(elf1_range) or unioned == set(elf2_range):
        cur_sum += 1
    elif intersection != set():
        cur_sum += 1
print(cur_sum)
