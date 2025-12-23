
FNAME = "2015/puzzle_input/d16.txt"


def new_sue():
    d = dict()
    d["children"] = -1
    d["cats"] = -1
    d["samoyeds"] = -1
    d["pomeranians"] = -1
    d["akitas"] =  -1
    d["vizslas"] =  -1
    d["goldfish"] = -1
    d["trees"] = -1
    d["cars"] = -1
    d["perfumes"] = -1
    return d

known_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

with open(FNAME, "r", encoding="UTF-8") as f:
    sues = []
    for line in f:
        first_colon = line.find(": ")
        line = line[first_colon + 2:-1]
        data = line.split(", ")
        ns = new_sue()
        for d in data:
            thing, amount = d.split(": ")
            if thing not in ns:
                raise ValueError(thing)
            ns[thing] = int(amount)
        sues.append(ns)
        # print(line)


# p1
for i, sue in enumerate(sues):
    cur = 0
    for key in sue:
        if sue[key] < 0 or known_sue[key] == sue[key]:
            cur += 1
    if cur == len(known_sue):
        print(i + 1)

# p2
for i, sue in enumerate(sues):
    cur = 0
    for key in sue:
        if sue[key] < 0:
            cur += 1
        elif key in ("cats", "trees") and sue[key] > known_sue[key]:
            cur += 1
        elif key in ("pomeranians", "goldfish") and sue[key] < known_sue[key]:
            cur += 1
        elif key not in ("cats", "trees", "pomeranians", "goldfish") and sue[key] == known_sue[key]:
            cur += 1
    if cur == len(known_sue):
        print(i + 1)
