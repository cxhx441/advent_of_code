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
                seeds_vals = [int(x) for x in l[7:].split(" ")]
                seeds = []
                i = 0
                while i < len(seeds_vals):
                    start = seeds_vals[i]
                    end = start + seeds_vals[i+1]
                    seeds.append(range(start, end))
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

    def get_new_ranges(map_name, starters):
        cur = starters.copy()
        while cur != []:
            start_rng = cur.pop()
            s_low = start_rng[0]
            s_high = start_rng[1]
            for dest_rng, modifier in maps[map_name].items():
                # if all in, convert all
                if s_low >= dest_rng[0] and s_high <= dest_rng[1]:
                    new_rng = range(s_low + modifier, s_high + modifier)
                # if all out, skip
                if s_high < dest_rng[0] or dest_rng[1] < s_low:
                    continue
                # if start range overshadows dest range
                if start_rng[0] < dest_rng[0] and start_rng[1] > dest_rng[1]:
                # if higher section of start is in lower section of dest...
                # if lower section of start is in higher section of dest...

            start_rng = "handled"


        return start

    soil = get_new_ranges(map_order[0], seeds)
    fertilizer = [get_dest(map_order[1], x) for x in soil]
    water = [get_dest(map_order[2], x) for x in fertilizer]
    light = [get_dest(map_order[3], x) for x in water]
    temp = [get_dest(map_order[4], x) for x in light]
    humidity = [get_dest(map_order[5], x) for x in temp]
    loc = [get_dest(map_order[6], x) for x in humidity]

    return loc
print(min(solution("2023//d5p2_input_ex.txt")))
print(min(solution("2023//d5p2_input.txt")))
