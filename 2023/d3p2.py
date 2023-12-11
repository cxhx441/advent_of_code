def solution(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        data = []
        for l in f:
            data.append(l[:-1])

    # def get_right_bound():
    #     right_bound = j
    #     while right_bound < len(r) and r[right_bound].isdigit():
    #         right_bound += 1
    #     return right_bound

    # def get_neighbors():
    #     n_set = set()
    #     for x in range(j-1, right_bound+1):
    #         n_set.add((i-1, x)) # add row above
    #         n_set.add((i+1, x)) # add row below
    #     n_set.add((i, j-1)) # add left
    #     n_set.add((i, right_bound)) # add right

    #     # remove out of bounds
    #     to_remove = set()
    #     for n in n_set:
    #         if n[0] < 0 or n[0] >= len(data) or n[1] < 0 or n[1] >= len(data[0]):
    #             to_remove.add(n)

    #     for n in to_remove:
    #         n_set.remove(n)

    #     return n_set

    def get_number_neighbors():
        seen = set()
        nums = []
        for neig in ( (i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j+1), (i+1, j-1)):
            if neig[0] in range(0, len(data)) and neig[1] in range(0, len(data[0])):
                if data[neig[0]][neig[1]].isdigit():
                    left = right = neig[1]
                    while left >= 0 and data[neig[0]][left-1].isdigit():
                        left -= 1
                    while right < len(data[0]) and data[neig[0]][right].isdigit():
                        right += 1

                    done = False
                    for x in range(right-left):
                        if (neig[0], left + x) in seen:
                            done = True

                    if not done:
                        for x in range(right - left):
                            seen.add((neig[0], left + x))

                        nums.append(int(data[neig[0]][left:right]))

        return nums


    def get_gear_ratio():
        num_neig = get_number_neighbors()
        if len(num_neig) == 2:
            return num_neig[0] * num_neig[1]
        return 0


    summ = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '*':
                summ += get_gear_ratio()
    # i = summ = 0
    # for r in data:
    #     j = 0
    #     while j < len(data[0]):
    #         right_bound = 0
    #         if data[i][j].isdigit():
    #             right_bound = get_right_bound()
    #             neighbors = get_neighbors()
    #             for n in neighbors:
    #                 if data[n[0]][n[1]] not in '0123456789.':
    #                     summ += int(data[i][j:right_bound])
    #                     break
    #         if j+right_bound > j+1:
    #             j = right_bound
    #         else:
    #             j += 1
    #     i += 1

    return summ

print(solution("2023//d3p2_input_ex.txt"))
print(solution("2023//d3p2_input.txt"))
