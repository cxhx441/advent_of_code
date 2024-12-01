from timeit import default_timer as timer
import collections
def solution(filename):
    left_data = []
    right_counts = collections.defaultdict(lambda: 0)
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            l, r = line[:-1].split("   ")
            left_data.append(int(l))
            right_counts[int(r)] += 1

    result = 0
    for l in left_data:
        result += l * right_counts[l]
    return result

FILENAME = "2024//d1p1_input_ex.txt" # expecting 31
print(solution(FILENAME))
assert solution(FILENAME) == 31

start = timer()
FILENAME = "2024//d1p1_input.txt"
result = solution(FILENAME)
end = timer()
print( f"{round(( end - start ) * 1000, 3)}ms" )
print(result)
