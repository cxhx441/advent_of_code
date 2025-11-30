from timeit import default_timer as timer

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            for i, el in enumerate(line[:-1]):
                continue
    return 0

def solution_1(x):
    return 0


def solution_2(x):
    return 0

if __name__ == "__main__":
    pass
    # start = timer()
    # input = parse_input("puzzle_input//d#_input.txt")
    # result = solution_1(input)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution1: {result}')


    # start = timer()
    # input = parse_input("puzzle_input//d#_input.txt")
    # result_2 = solution_2(input)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution2: {result_2}')
