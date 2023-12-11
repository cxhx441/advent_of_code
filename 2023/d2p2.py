from copy import deepcopy

def solution(filename):
    games = [None]
    with open(filename, 'r', encoding="UTF-8") as f:
        for game in f:
            cur_game = []
            game = game.split(': ')[1][:-1] # get rid of 'game: ' and newline
            game_sets = game.split(';')
            for g_s in game_sets:
                game_set = {"red": 0, "green": 0, "blue": 0}
                colors = g_s.split(", ")
                for c in colors:
                    if "red" in c:
                        val = c[:len(c) - len("red")]
                        game_set["red"] += int(val)
                    elif "green" in c:
                        val = c[:len(c) - len("green")]
                        game_set["green"] += int(val)
                    elif "blue" in c:
                        val = c[:len(c) - len("blue")]
                        game_set["blue"] += int(val)
                cur_game.append(game_set.copy())
            games.append(deepcopy(cur_game))

    summ = 0
    for i, g in enumerate(games):
        if i == 0:
            continue

        min_reqd = {"red": 0, "green": 0, "blue": 0}
        for s in g:
            min_reqd["red"] = max(min_reqd["red"], s["red"])
            min_reqd["green"] = max(min_reqd["green"], s["green"])
            min_reqd["blue"] = max(min_reqd["blue"], s["blue"])

        power = min_reqd["red"] * min_reqd["green"] * min_reqd["blue"]
        summ += power

    return summ

print(solution("2023//d2p2_input_ex.txt"))
print(solution("2023//d2p2_input.txt"))
