import string

def get_data(infile):
    with open(infile, 'r') as f:
        return f.readline()[:-1]

this_file = "real_input.txt"
line = get_data(this_file)

window_map = {x: 0 for x in string.ascii_lowercase}
unique_sum = 0
goal = 14
for i in range(goal):
    if window_map[line[i]] == 0:
        unique_sum += 1
    window_map[line[i]] += 1

i = goal
while unique_sum < goal and i < len(line):
    # if unique letter in window is leaving, decrement unique count
    if window_map[line[i-goal]] == 1:
        unique_sum -= 1
    window_map[line[i-goal]] -= 1

    # if unique letter is entering window, increment unique count
    if window_map[line[i]] == 0:
        unique_sum += 1
    window_map[line[i]] += 1

    i += 1

print(i)


with open('input.txt') as file:
    s = file.readlines()

for i in range(3, len(s[0])):
    if s[0][i] not in s[0][i-3:i] and s[0][i-1] not in s[0][i-3:i-1] and s[0][i-2] != s[0][i-3]:
        print(i+1)
        break

for i in range(13, len(s[0])):
    f = True
    for j in range(14):
        if s[0][i-j] in s[0][i-13:i-j]:
            f = False
            break
    if f:
        print(i+1)

