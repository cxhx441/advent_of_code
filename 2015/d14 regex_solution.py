import re
from collections import defaultdict, Counter
import itertools

FNAME = "2015/puzzle_input/d14.txt"
FINISH_TIMESTAMP = 2503

# FNAME = "2015/puzzle_input/d14ex.txt";
# FINISH_TIMESTAMP = 1000

reindeers = set()
history = defaultdict(list)
with open(FNAME, "r", encoding="UTF-8") as f:
    txt = f.read()
    regex = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    for who, speed, duration, rest in re.findall(regex, txt):
        steps = itertools.cycle( [int(speed)]*int(duration) + [0]*int(rest) )
        history[who] = list( itertools.accumulate(next(steps) for _ in range (FINISH_TIMESTAMP) ) )

by_dist = max(h[-1] for h in history.values())
print(by_dist)


x = zip(*history.values())

scored = [ i for a in zip(*history.values()) for i, v in enumerate(a) if v == max(a) ]
by_points = max(Counter(scored).values())
print(by_points)
