from timeit import default_timer as timer
import math

valid_chars = { x for x in '1234567890()' }
def get_next_mul(s, i):
    start = s.find("mul(", i)
    if start == -1:
        return 0, i + 1

    end = s.find(")", start)
    if end == -1:
        return 0, i + 1

    operand = s[start + len("mul(") : end]

    if ',' not in operand:
        return 0, i + 1

    ops = operand.split(',')
    if len(ops) > 2:
        return 0, i + 1

    try:
        return int(ops[0]) * int(ops[1]), end + 1
    except ValueError:
        return 0, i + 1

# def validate_op(operand):

def get_total(data):
    i = 0
    total = 0
    while i < len(data):
        result, new_beginning = get_next_mul(data, i)
        total += result
        i = new_beginning

    return total

def solution(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        data = []
        for line in f:
            data.append(line[:-1])

    data = "".join(data)
    return get_total("".join(data))


# filename = "2024//d3p1_input_ex.txt"
# assert solution(filename) == 161

start = timer()
filename = "2024//d3p1_input.txt"
result = solution(filename)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result)
