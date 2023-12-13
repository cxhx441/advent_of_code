def solution(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        data = []
        for l in f:
            data.append(l[l.index(":") + 1 : -1])

    cards = []
    for card in data:
        winning_nums, my_nums = card.split(" | ")
        winning_nums = winning_nums.split(" ")
        my_nums = my_nums.split(" ")
        winning_nums = set([int(x) for x in winning_nums if x != ""])
        my_nums = [int(x) for x in my_nums if x != ""]
        cards.append([winning_nums.copy(), my_nums.copy()])

    winnings = 0
    for c in cards:
        winning_nums_cnt = 0
        for w in c[1]:
            if w in c[0]:
                winning_nums_cnt += 1

        if winning_nums_cnt > 0:
            winnings += 2 ** (winning_nums_cnt - 1)
        # print(c)

    return winnings


print(solution("2023//d4p1_input_ex.txt"))
print(solution("2023//d4p1_input.txt"))
