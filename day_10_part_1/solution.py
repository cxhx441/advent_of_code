
# addx V = 2 cycles
    # x register increases by V

# noop = 1 cycle
    # no effect

# signal strength = cycle_number * value of x register


def addx(x, regx, during_cycle_vals, cycle_num):
    during_cycle_vals.append(regx[0])
    cycle_num += 1
    during_cycle_vals.append(regx[0])
    cycle_num += 1
    regx[0] += x
    return cycle_num

def noop(regx, during_cycle_vals, cycle_num):
    during_cycle_vals.append(regx[0])
    return cycle_num + 1


during_cycle_values = [1] # regx[i] = value and cycle i
regx = [1]
infile = "sample_input.txt"
infile = "sample_input 2.txt"
infile = "real_input.txt"
cycle_num = 1
with open(infile, 'r') as f:
    for line in f:
        if line[:-1] == 'noop':
            cycle_num = noop(regx, during_cycle_values, cycle_num)
        else:
            command, x = line[:-1].split(' ')
            cycle_num = addx(int(x), regx, during_cycle_values, cycle_num)
during_cycle_values.append(regx[0])


print(during_cycle_values)
for i in range(20, len(during_cycle_values), 40):
    print(i, during_cycle_values[i])

print()
val = 0
for i in range(20, 221, 40):
    val += i * during_cycle_values[i]
    print(i, during_cycle_values[i])

print(val)

# val = 0
# regx = 1
# cycle_num = 1
# with open(infile, 'r') as f:
#     for line in f:
#         if line[:-1] == 'noop':
#             if condition_is_met(cycle_num):
#                 print(cycle_num, regx)
#                 val += regx*cycle_num
#             cycle_num += 1
#         else:
#             command, x = line[:-1].split(' ')
#             if condition_is_met(cycle_num):
#                 print(cycle_num, regx)
#                 val += regx*cycle_num
#             cycle_num += 1
#             if condition_is_met(cycle_num):
#                 print(cycle_num, regx)
#                 val += regx*cycle_num
#             cycle_num += 1
#             regx += int(x)

