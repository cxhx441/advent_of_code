
FNAME = "2015/puzzle_input/d14.txt"
FINISH_TIMESTAMP = 2503

# FNAME = "2015/puzzle_input/d14ex.txt";
# FINISH_TIMESTAMP = 1000

class Reindeer:
    def __init__(self):
        self.name = ""
        self.speed = 0
        self.speed_period = 0
        self.rest_period = 0
        self.location = 0
        self.speed_progress_remaining = 0
        self.rest_progress_remaining = 0
        self.points = 0

    def increment(self):
        if self.rest_progress_remaining > 0:
            self.rest_progress_remaining -= 1
            if self.rest_progress_remaining == 0:
                self.speed_progress_remaining = self.speed_period

        elif self.speed_progress_remaining > 0:
            self.speed_progress_remaining -= 1
            self.location += self.speed
            if self.speed_progress_remaining == 0:
                self.rest_progress_remaining = self.rest_period



reindeers = set()
with open(FNAME, "r", encoding="UTF-8") as f:
    for line in f:
        line = line.split(" ")
        r = Reindeer()
        r.name = line[0]
        r.speed = int(line[3])
        r.speed_period = int(line[6])
        r.speed_progress_remaining = int(line[6])
        r.rest_period = int(line[13])
        reindeers.add(r)

for i in range(FINISH_TIMESTAMP):
    max_location = 0
    for r in reindeers:
        r.increment()
        max_location = max(max_location, r.location)

    for r in reindeers:
        if r.location == max_location:
            r.points += 1
    #     print(f"{i + 1}s: {r.name}, {r.points}")
    # print()



for r in reindeers:
    print(r.name, r.points)
