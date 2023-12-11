def solution(filename):
    data = []
    with open(filename, 'r', encoding="UTF-8") as f:
        for l in f:
            data.append(l[:-1])

    print(data)

    def get_value(s: str):
        l = 0
        r = len(s) - 1
        while l < r and not s[l].isdigit():
            l += 1

        val = int(s[l])*10

        while r > l and not s[r].isdigit():
            r -= 1

        return val + int(s[r])



    summed = 0
    for d in data:
        summed += get_value(d)

    return summed

filename = "2023//d1p1_input_ex.txt" # expecting 142
assert solution(filename) == 142

filename = "2023//d1p1_input.txt" # expecting 142
print(solution(filename))
