from timeit import default_timer as timer
import math

valid_chars = { x for x in '1234567890()' }

def get_next_mul(s, i, do_flag):
    if do_flag is False:
        next_do = s.find("do()", i)
        if next_do != -1:
            return 0, next_do + 1, True
        return 0, i + 1, do_flag

    next_dont = s.find("don't()", i)
    start = s.find("mul(", i)
    if start == -1:
        return 0, i + 1, do_flag

    if next_dont != -1 and next_dont < start:
        return 0, i + 1, False

    end = s.find(")", start)
    if end == -1:
        return 0, i + 1, do_flag

    operand = s[start + len("mul(") : end]

    if ',' not in operand:
        return 0, i + 1, do_flag

    ops = operand.split(',')
    if len(ops) > 2:
        return 0, i + 1, do_flag

    try:
        return int(ops[0]) * int(ops[1]), end + 1, do_flag
    except ValueError:
        return 0, i + 1, do_flag

# def validate_op(operand):

def get_total(data):
    i = 0
    total = 0
    do_flag = True
    while i < len(data):
        result, new_beginning, do_flag = get_next_mul(data, i, do_flag)
        total += result
        i = new_beginning
        print(i)

    return total

def solution(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        data = []
        for line in f:
            data.append(line[:-1])

    data = "".join(data)
    return get_total(data)


# filename = "2024//d3p2_input_ex.txt"
# assert solution(filename) == 48

start = timer()
filename = "2024//d3p2_input.txt"
result = solution(filename)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result)
