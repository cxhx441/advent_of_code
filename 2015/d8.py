
# n_chars_in_str - n_chars_in_memory = return_value
def count_pt1(line):
    n_chars_in_str = len(line)
    n_chars_in_mem = n_chars_in_str -2 # remove bookend double quotes.
    n = len(line)
    i = 0
    while i < n:
        if i + 2 <= n and line[i:i+2] == "\\\\" or line[i:i+2] == "\\\"":
            i += 1
            n_chars_in_mem -= 1
        elif i + 4 <= n and line[i:i+2] == "\\x":
            i += 3
            n_chars_in_mem -= 3
        i += 1
    this_line_result = n_chars_in_str - n_chars_in_mem
    print(f"{n_chars_in_str} - {n_chars_in_mem} = {this_line_result}: {line}")
    return this_line_result

def count_pt2(line):
    total = 2 # start with two for additional double quotes bookending
    total += line.count("\\")
    total += line.count("\"")
    print(f"{total}: {line}")
    return total

def parse_pt1(fname):
    print()
    result = 0
    with open(fname, 'r', encoding="UTF-8") as f:
        for line in f:
            result += count_pt1(line[:-1])
    print(result)

def parse_pt2(fname):
    print()
    result = 0
    with open(fname, 'r', encoding="UTF-8") as f:
        for line in f:
            result += count_pt2(line[:-1])
    print(f"result : {result}")

# "\\"
# "\\\x80"
# "\\\\x80"

# parse_pt1("2015/puzzle_input/d8.txt")
# parse_pt1("2015/puzzle_input/d8_ex.txt")
# parse_pt2("2015/puzzle_input/d8.txt")
# parse_pt2("2015/puzzle_input/d8_ex.txt")
