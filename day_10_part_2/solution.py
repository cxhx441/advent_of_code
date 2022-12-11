
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

def print_screen(screen):
    for h in screen:
        for pxl in range(len(h)):
            s = f'{h[pxl]}'
            print(s, end='')
        print()

screen = [['.']*40 for _ in range(6)]

i = 1
for row in range(len(screen)):
    for col in range(len(screen[0])):
        if i < len(during_cycle_values):
            pixels = (during_cycle_values[i]-1, during_cycle_values[i], during_cycle_values[i]+1)
            if col in pixels:
                screen[row][col] = '#'
            i += 1

print_screen(screen)
