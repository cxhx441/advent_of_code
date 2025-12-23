import re
from collections import defaultdict, Counter
from itertools import product

FNAME = "2015/puzzle_input/d15.txt"
FNAME = "2015/puzzle_input/d15ex.txt";


class Ingrediant:
    def __init__(self, capacity, durability, flavor, texture, calories):
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)


    def __repr__(self):
        s = []
        s.append(f"capacity {self.capacity}")
        s.append(f"durability {self.durability}")
        s.append(f"flavor {self.flavor}")
        s.append(f"texture {self.texture}")
        s.append(f"calories {self.calories}")
        return ', '.join(s)

def amounts(total, k):
    if k == 1:
        yield [total]
    else:
        for i in range(total + 1):
            for rest in amounts(total - i, k - 1):
                yield [i] + rest

ingrediants = dict()

with open(FNAME, "r", encoding="UTF-8") as f:
    for line in f:
        name, props = line.split(": ")
        props = props.split(", ")

        capacity = props[0].split(" ")[1]
        durability = props[1].split(" ")[1]
        flavor = props[2].split(" ")[1]
        texture = props[3].split(" ")[1]
        calories = props[4].split(" ")[1]

        ingrediant = Ingrediant(capacity, durability, flavor, texture, calories)
        ingrediants[name] = ingrediant
        # combos = get_combos(len(ingrediants), 100)
        # for a in range(TOTAL + 1):
        #     for b in range(TOTAL - a + 1):
        #         for c in range(TOTAL - a - b + 1):
        #             for d in range(TOTAL - a - b - c + 1):

    TOTAL = 100
    ingr_list = [ x for x in ingrediants.values() ]
    result = 0
    for amount in amounts(TOTAL, len(ingrediants)):
        cur = 0
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        calories = 0
        # print(amount)
        for a, ingr in zip(amount, ingr_list):
            capacity += ingr.capacity * a
            durability += ingr.durability * a
            flavor += ingr.flavor * a
            texture += ingr.texture * a
            calories += ingr.calories * a
        if calories == 500:
            cur = max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)
            result = max(result, cur)

    print(result)



