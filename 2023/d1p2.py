def solution(file):
    data = []
    with open(file, 'r', encoding="UTF-8") as f:
        for l in f:
            data.append(l[:-1])
    def check_str_digit(s: str):
        valid_strs = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }
        for j in range(3, 6):
            if j <= len(s) and s[:j] in valid_strs.keys():
                return valid_strs[s[:j]]
        return None

    def get_value(s: str):
        l = 0
        r = len(s) - 1
        val = None
        while l < r and not s[l].isdigit() and val is None:
            val = check_str_digit(s[l:])
            l += 1
        if val is None:
            val = int(s[l])
        val *= 10

        singles_place = None
        while r > l and not s[r].isdigit() and singles_place is None:
            singles_place = check_str_digit(s[r:])
            r -= 1

        if singles_place is not None:
            val += singles_place
        else:
            val += int(s[r])

        return val

    summed = 0
    for d in data:
        summed += get_value(d)

    return summed

filename = "2023//d1p2_input_ex.txt" # expecting 142
#assert solution(filename) == 281
print(solution(filename))

filename = "2023//d1p2_input.txt" # expecting 142
print(solution(filename))
