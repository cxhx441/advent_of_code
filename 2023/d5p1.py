def solution(filename):
    map_order = ["seed-to-soil map",
                "soil-to-fertilizer map",
                "fertilizer-to-water map",
                "water-to-light map",
                "light-to-temperature map",
                "temperature-to-humidity map",
                "humidity-to-location map",
                ]
    map_order_set = set(map_order)
    maps = {
        map_order[0]: {},
        map_order[1]: {},
        map_order[2]: {},
        map_order[3]: {},
        map_order[4]: {},
        map_order[5]: {},
        map_order[6]: {},
    }

    with open(filename, "r", encoding="UTF-8") as f:
        map_name = None
        for l in f:
            if l[:7] == "seeds: ":
                seeds = [int(x) for x in l[7:].split(" ")]
            elif l[:-2] in map_order_set:
                map_name = l[:-2]
            elif l != "\n":
                # x, y, z = dest, start, ran
                x, y, z = [int(x) for x in l[:-1].split(" ")]
                maps[map_name][range(y,  y + z + 1)] = x - y

    def get_dest(map_name, start):
        for rng, modifier in maps[map_name].items():
            if start in rng:
                return start + modifier
        return start

    soil = [get_dest(map_order[0], x) for x in seeds]
    fertilizer = [get_dest(map_order[1], x) for x in soil]
    water = [get_dest(map_order[2], x) for x in fertilizer]
    light = [get_dest(map_order[3], x) for x in water]
    temp = [get_dest(map_order[4], x) for x in light]
    humidity = [get_dest(map_order[5], x) for x in temp]
    loc = [get_dest(map_order[6], x) for x in humidity]

    return loc
print(min(solution("2023//d5p1_input_ex.txt")))
print(min(solution("2023//d5p1_input.txt")))
