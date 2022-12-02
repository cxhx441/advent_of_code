def input_to_list(infile):
    matches = []
    input_to_throws = {
        "X": "LOSE",
        "Y": "DRAW",
        "Z": "WIN",
        "A": "ROCK",
        "B": "PAPER",
        "C": "SCISSORS"
    }
    with open(infile, 'r') as f:
        for line in f:
            them = input_to_throws[line[0]]
            outcome = input_to_throws[line[-2]]
            if outcome == "WIN":
                me = win_dic[them]
            elif outcome == "LOSE":
                me = lose_dic[them]
            else:
                me = them
            matches.append((them, me))
    return matches

throw_score = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}

win_dic = {
    "ROCK": "PAPER",
    "PAPER": "SCISSORS",
    "SCISSORS": "ROCK"
}
lose_dic = {
    "ROCK": "SCISSORS",
    "PAPER": "ROCK",
    "SCISSORS": "PAPER"
}
win_conditions = [("ROCK", "PAPER"), ("PAPER", "SCISSORS"), ("SCISSORS", "ROCK")] # them, me

matches = input_to_list("sample_input.txt") # 15
# matches = input_to_list("real_input.txt") #

total_score = 0
for match in matches:
    them, me = match
    total_score += throw_score[me]

    if match in win_conditions: # win
        total_score += 6
    elif match[0] == match[1]: # draw
        total_score += 3

print(total_score)





# print(data)
