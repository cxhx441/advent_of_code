from collections import defaultdict
from timeit import default_timer as timer
import re

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        # for line in f:
        #     for i, el in enumerate(line[:-1]):
        #         continue
        data = f.read().strip()
        pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
        matches = re.findall(pattern, data)
        results = [{"p": [int(x1), int(y1)], "v": [int(x2), int(y2)], "xmas_list": []} for x1, y1, x2, y2 in matches]
    return results

def solution_1(data, rows, cols, seconds):
    quadrants_count = [0] * 4
    for i in range(len(data)):
        data[i]["p"][0] += data[i]['v'][0] * seconds
        data[i]["p"][1] += data[i]['v'][1] * seconds

        data[i]["p"][0] = data[i]["p"][0] % cols
        data[i]["p"][1] = data[i]["p"][1] % rows

        if data[i]["p"][0] < cols // 2:
            if data[i]["p"][1] < rows // 2:
                quadrants_count[0] += 1
            if data[i]["p"][1] > rows // 2:
                quadrants_count[1] += 1
        if data[i]["p"][0] > cols // 2:
            if data[i]["p"][1] < rows // 2:
                quadrants_count[2] += 1
            if data[i]["p"][1] > rows // 2:
                quadrants_count[3] += 1

    total = 1
    for c in quadrants_count:
        total *= c
    return total



def solution_2(data, rows, cols, limit=float("inf")):
    log = defaultdict(int)
    for i in range(len(data)):
        p = data[i]["p"]
        log[tuple(p)] += 1

    time = 0
    while True:
        for i in range(len(data)):
            p = (data[i]["p"][0], data[i]["p"][1])
            log[p] -= 1

            data[i]["p"][0] += data[i]['v'][0]
            data[i]["p"][1] += data[i]['v'][1]
            data[i]["p"][0] = data[i]["p"][0] % cols
            data[i]["p"][1] = data[i]["p"][1] % rows

            p = (data[i]["p"][0], data[i]["p"][1])
            log[p] += 1
        time += 1

        haves = {x for x in log if log[x] > 0}
        if len(haves) == 500:
            with open('out.txt', 'a') as out_file:
                print(time, file=out_file)
                print(time)
                # printit()
                for r in range(rows):
                    for c in range(cols):
                        if (c, r) in haves:
                            print('*', end='', file=out_file)
                        else:
                            print('.', end='', file=out_file)
                    print("", file=out_file)
                print(file=out_file)

if __name__ == "__main__":
    # start = timer()
    # data = parse_input("puzzle_input//d14_input.txt")
    # result = solution_1(data, 103, 101, 100)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution1: {result}')


    start = timer()
    data = parse_input("puzzle_input//d14_input.txt")
    solution_2(data, 103, 101)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
