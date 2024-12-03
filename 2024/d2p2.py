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

        def good_sub_rpt(sub_rpt):
            diff = sub_rpt[1] - sub_rpt[0]
            if abs(diff) == 0 or abs(diff) > 3:
                return False

            direction = sign(diff)
            for i in range(1, len(sub_rpt)):
                cur_diff = sub_rpt[i] - sub_rpt[i-1]
                cur_dir = sign(cur_diff)
                if cur_dir != direction or abs(cur_diff) == 0 or abs(cur_diff) > 3:
                    return False
            return True

        if good_sub_rpt(report):
            return True

        for i in range(len(report)):
            sub_rpt = report[:i] + report[i+1:]
            if good_sub_rpt(sub_rpt):
                return True
        return False

    safe_cnt = 0
    for report in data:
        if good_rpt(report):
            safe_cnt += 1

    return safe_cnt

filename = "2024//d2p1_input_ex.txt" # expecting 2
result = solution(filename)
print(result)
assert result == 4

start = timer()
filename = "2024//d2p1_input.txt"
result = solution(filename)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result)
