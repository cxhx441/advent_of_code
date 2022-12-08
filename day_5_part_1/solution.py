def get_stacks(infile):
    with open(infile, 'r') as f:
        for line in f:
            if line[1] != '1':
                continue
            else:
                return {int(x):[] for x in line[:-1].split(' ') if x != ''}
def fill_stacks(stacks, infile):
    with open(infile, 'r') as f:
        for line in f:
            if line[1] == '1':
                for stack in stacks.values():
                    stack.reverse()
                return stacks
            stack_num = 1
            for i in range(1, len(line[:-1]), 4):
                if line[i] != ' ':
                    stacks[stack_num].append(line[i])
                stack_num += 1

def get_commands(infile):
    commands = []
    with open(infile, 'r') as f:
        for line in f:
            if line[:4] != 'move':
                continue
            line = line[:-1]
            line = line.replace('move ', '')
            line = line.replace('from ', '')
            line = line.replace('to ', '')
            line = line.split(' ')
            command = tuple([int(x) for x in line])
            commands.append(command)
        return commands




this_file = "sample_input.txt"
this_file = "real_input.txt"
stacks = get_stacks(this_file) #
stacks = fill_stacks(stacks, this_file)
commands = get_commands(this_file)
# data = input_to_list("real_input.txt") #
print(stacks)
print(stacks)
print(commands)
for command in commands:
    count, from_stack, to_stack = command
    for i in range(count):
        stacks[to_stack].append(stacks[from_stack].pop())

for stack in stacks.values():
    if len(stack) > 0:
        print(stack[-1], end='')



