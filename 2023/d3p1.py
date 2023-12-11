def solution(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        data = []
        for l in f:
            data.append(l[:-1])

    def get_right_bound():
        right_bound = j
        while right_bound < len(r) and r[right_bound].isdigit():
            right_bound += 1
        return right_bound

    def get_neighbors():
        n_set = set()
        for x in range(j-1, right_bound+1):
            n_set.add((i-1, x)) # add row above
            n_set.add((i+1, x)) # add row below
        n_set.add((i, j-1)) # add left
        n_set.add((i, right_bound)) # add right

        # remove out of bounds
        to_remove = set()
        for n in n_set:
            if n[0] < 0 or n[0] >= len(data) or n[1] < 0 or n[1] >= len(data[0]):
                to_remove.add(n)

        for n in to_remove:
            n_set.remove(n)

        return n_set

    i = summ = 0
    for r in data:
        j = 0
        while j < len(data[0]):
            right_bound = 0
            if data[i][j].isdigit():
                right_bound = get_right_bound()
                neighbors = get_neighbors()
                for n in neighbors:
                    if data[n[0]][n[1]] not in '0123456789.':
                        summ += int(data[i][j:right_bound])
                        break
            if j+right_bound > j+1:
                j = right_bound
            else:
                j += 1
        i += 1



    return summ


print(solution("2023//d3p1_input_ex.txt"))
print(solution("2023//d3p1_input.txt"))
