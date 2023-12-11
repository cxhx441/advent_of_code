from copy import deepcopy

def solution(filename, p_red, p_green, p_blue):
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

    possible_games_id_sum = 0
    for i, g in enumerate(games):
        if i == 0:
            continue
        possible = True
        for s in g:
            if s["red"] > p_red or s["green"] > p_green or s["blue"] > p_blue:
                possible = False
                break
        if possible is True:
            possible_games_id_sum += i

    return possible_games_id_sum

print(solution("2023//d2p1_input_ex.txt", 12, 13, 14))
print(solution("2023//d2p1_input.txt", 12, 13, 14))
