from timeit import default_timer as timer
import math
def solution(filename):
    data = []
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            report = [ int(lvl) for lvl in line[:-1].split(" ") ]
            data.append(report)

    def sign(num):
        return "-" if num < 0 else '+'

    def good_rpt(report):
        diff = report[1] - report[0]
        if diff == 0:
            return False

        direction = sign(diff)
        for i in range(1, len(report)):
            cur_diff = report[i] - report[i-1]
            cur_dir = sign(cur_diff)
            if cur_dir != direction or abs(cur_diff) == 0 or abs(cur_diff) > 3:
                return False
        return True

    safe_cnt = 0
    for report in data:
        if good_rpt(report):
            safe_cnt += 1

    return safe_cnt

filename = "2024//d2p1_input_ex.txt" # expecting 2
assert solution(filename) == 2

start = timer()
filename = "2024//d2p1_input.txt"
result = solution(filename)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result)
