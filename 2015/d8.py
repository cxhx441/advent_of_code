


# n_chars_in_str - n_chars_in_memory = return_value
def doit(fname):
    print()
    result = 0
    with open(fname, 'r', encoding="UTF-8") as f:
        for line in f:
            line = line[:-1]
            n_chars_in_str = len(line)
            nhex = line.count("\\x")
            nbackslash = line.count("\\\\")
            ndoublequote = line.count("\\\"")
            n_chars_in_mem = ( n_chars_in_str - nhex*3 - nbackslash - ndoublequote) - 2
            this_line_result = n_chars_in_str - n_chars_in_mem
            print(f"{n_chars_in_str} - {n_chars_in_mem} = {this_line_result}: {line}")
            result += this_line_result
    print(result)

# doit("2015/puzzle_input/d8.txt")
doit("2015/puzzle_input/d8_ex.txt")
# 1349 too high
# 1234 too low
# 749 too low
