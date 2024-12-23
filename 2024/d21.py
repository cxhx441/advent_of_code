from timeit import default_timer as timer
import networkx as nx
import collections

KEYPAD = [ ['7', '8', '9'],
           ['4', '5', '6'],
           ['1', '2', '3'],
           [' ', '0', 'A']]

DPAD =   [ [' ', '^', 'A'],
           ['<', 'v', '>'] ]


def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        codes = []
        for line in f:
            codes.append(line.strip())
    return codes

keypad_paths = []
dpad_paths = []
def solution_1():

    return 0

def solution_2():
    return 0


if __name__ == "__main__":
    start = timer()
    codes = parse_input("puzzle_input/d21_input.txt")
    complexity = solution_1(codes)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {complexity}')

    # start = timer()
    # racetrack = parse_input("puzzle_input/d20_input.txt")
    # result = solution_2(racetrack, 100)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution1: {result}')

