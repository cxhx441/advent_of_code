from timeit import default_timer as timer

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            for i, el in enumerate(line[:-1]):
                continue
    return 0

def solution_1(x):
    return 0

input = parse_input("2024//puzzle_input//d#_input_ex.txt")
result_1 = solution_1(input)
print(result_1)
assert result_1 == 41

# start = timer()
# input = parse_input("2024//puzzle_input//d#_input.txt")
# result = solution_2(input)
# print(result)
# end = timer()
# print( f"{( end - start ) * 1000}ms" )
# print(result)


# def solution_2(x):
#     return 0

# input = parse_input("2024//puzzle_input//d#_input_ex.txt")
# result_2 = solution_1(input)
# print(result_2)
# assert result_2 == 41

# start = timer()
# input = parse_input("2024//puzzle_input//d#_input.txt")
# result_2 = solution_2(input)
# print(result_2)
# end = timer()
# print( f"{( end - start ) * 1000}ms" )
# print(result_2)
