from timeit import default_timer as timer

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        test_val_arr = []
        inputs_arr = []
        for line in f:
            line = line[:-1]
            test_val, inputs = line.split(": ")
            test_val_arr.append(int(test_val))
            inputs_arr.append( [ int(x) for x in inputs.split(" ") ] )
    return test_val_arr, inputs_arr

def solution_1(data):
    test_val_arr, input_arr = data
    def backtrack(i, total):
        if i == len(inputs):
            if total == test_val:
                return True
            return False

        if backtrack(i + 1, total + inputs[i]):
            return True
        if backtrack(i + 1, total * inputs[i]):
            return True
        return False

    valid = 0
    for test_val, inputs in zip(test_val_arr, input_arr):
        if backtrack(1, inputs[0]):
            valid += test_val

    return valid

input = parse_input("2024//puzzle_input//d7_input_ex.txt")
result_1 = solution_1(input)
print(result_1)
assert result_1 == 3749

start = timer()
input = parse_input("2024//puzzle_input//d7_input.txt")
result = solution_1(input)
print(result)
end = timer()
print( f"{( end - start ) * 1000}ms" )

def solution_2(data):
    test_val_arr, input_arr = data
    def backtrack(i, total):
        if i == len(inputs):
            if total == test_val:
                return True
            return False

        if backtrack(i + 1, total + inputs[i]):
            return True
        if backtrack(i + 1, total * inputs[i]):
            return True
        if backtrack(i + 1, int( f'{total}{inputs[i]}' )):
            return True

        return False

    valid = 0
    for test_val, inputs in zip(test_val_arr, input_arr):
        if backtrack(1, inputs[0]):
            valid += test_val

    return valid

input = parse_input("2024//puzzle_input//d7_input_ex.txt")
result_1 = solution_2(input)
print(result_1)
assert result_1 == 11387

start = timer()
input = parse_input("2024//puzzle_input//d7_input.txt")
result = solution_2(input)
print(result)
end = timer()
print( f"{( end - start ) * 1000}ms" )
