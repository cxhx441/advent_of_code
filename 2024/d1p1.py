from timeit import default_timer as timer
def solution(filename):
    left_data = []
    right_data = []
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            l, r = line[:-1].split("   ")
            left_data.append(int(l))
            right_data.append(int(r))

    left_data.sort()
    right_data.sort()
    result = 0
    for l, r in zip(left_data, right_data):
        result += abs(l - r)
    return result

filename = "2024//d1p1_input_ex.txt" # expecting 11
print(solution(filename))
# assert solution(filename) == 11

start = timer()
filename = "2024//d1p1_input.txt"
result = solution(filename)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result)
