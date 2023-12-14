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
                    i += 2
            elif l[:-2] in map_order_set:
                map_name = l[:-2]
            elif l != "\n":
                # x, y, z = dest, start, ran
                x, y, z = [int(x) for x in l[:-1].split(" ")]
                maps[map_name][range(y,  y + z + 1)] = x - y

    # def get_dest(map_name, start):
    #     for rng, modifier in maps[map_name].items():
    #         if start in rng:
    #             return start + modifier
    #     return start

    def get_new_ranges(map_name, starters):
        cur = starters.copy()
        new_ranges = []
        while cur != []:
            start_rng = cur.pop()
            s_low = start_rng[0]
            s_high = start_rng[-1]
            handled = False
            for dest_rng, modifier in maps[map_name].items():
                if handled:
                    break
                # if doesn't fit in any range, pass to
                d_low = dest_rng[0]
                d_high = dest_rng[-1]
                # if all out, skip
                if s_high < d_low or s_low > d_high:
                    continue
                # if all in, convert all
                elif s_low >= d_low and s_high <= d_high:
                    new_ranges.append(range(s_low + modifier, s_high + modifier + 1))
                    handled = True
                # if start range overshadows dest range
                elif s_low < d_low and s_high > d_high:
                    new_ranges.append(range(d_low + modifier, d_high + modifier + 1))
                    left_range_clipped = range(s_low, d_low)
                    right_range_clipped = range(d_high + 1, s_high + 1)
                    cur += [left_range_clipped, right_range_clipped]
                    handled = True
                # if higher section of start is in lower section of dest...
                elif s_high >= d_low and s_low < d_low:
                    new_ranges.append(range(d_low + modifier, s_high + modifier + 1))
                    cur += [range(s_low, d_low)]
                    handled = True
                # if lower section of start is in higher section of dest...
                elif s_low <= d_high and s_high > d_high:
                    new_ranges.append(range(s_low + modifier, d_high + modifier + 1))
                    cur += [range(d_high+1, s_high + 1)]
                    handled = True

            # no mapping
            if not handled:
                new_ranges.append(start_rng)

        return new_ranges

    soil = get_new_ranges(map_order[0], seeds)
    fertilizer = get_new_ranges(map_order[1], soil)
    water = get_new_ranges(map_order[2], fertilizer)
    light = get_new_ranges(map_order[3], water)
    temp = get_new_ranges(map_order[4], light)
    humidity = get_new_ranges(map_order[5], temp)
    loc = get_new_ranges(map_order[6], humidity)

    return loc
low = min([x[0] for x in solution("2023//d5p2_input_ex.txt")])
print(low)
#print(min(solution("2023//d5p2_input.txt")))
low = min([x[0] for x in solution("2023//d5p2_input.txt")])
print(low)
