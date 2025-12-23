from itertools import permutations
from bisect import bisect_left, bisect

FNAME = "2015/puzzle_input/d14.txt"
FINISH_TIMESTAMP = 2503

FNAME = "2015/puzzle_input/d14ex.txt";
FINISH_TIMESTAMP = 1000

speed = dict()
speed_dur = dict()
rest_dur = dict()
reindeers = set()
progression = dict()
with open(FNAME, "r", encoding="UTF-8") as f:
    for line in f:
        line = line.split(" ")
        name = line[0]
        speed[name] = int(line[3])
        speed_dur[name] = int(line[6])
        rest_dur[name] = int(line[13])
        reindeers.add(name)

for name in reindeers:
    prev_time, prev_dist = 0, 0
    while True:
        move_time = prev_time + speed_dur[name] + rest_dur[name]
        move_dist = prev_dist + speed[name] * speed_dur[name]
        if move_time > FINISH_TIMESTAMP:
            break
        prev_time, prev_dist = move_time, move_dist

    if prev_time + speed_dur[name] <= FINISH_TIMESTAMP:
        prev_time, prev_dist = (prev_time + speed_dur[name], prev_dist + speed[name] * speed_dur[name])
    else:
        while prev_time < FINISH_TIMESTAMP:
            prev_time += 1
            prev_dist += speed[name]
            print("entered")

    progression[name] = [prev_time, prev_dist]

farthest_dist = 0
farthest_reindeer = ''
print()
for name in reindeers:
    print(name)
    time, dist = progression[name]
    print(dist)

    if dist > farthest_dist:
        farthest_dist = dist
        farthest_reindeer = name

    print(name, time, dist)
    print()

print(f"results: {farthest_reindeer} at {farthest_dist}")
