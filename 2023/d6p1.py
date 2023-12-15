def solution(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        time = f.readline()
        time = time[len("Time: "):-1].split(" ")
        time = [int(x) for x in time if x != ""]
        distance = f.readline()
        distance = distance[len("Distance: "):-1].split(" ")
        distance = [int(x) for x in distance if x != ""]

    def dist_for_button_held(button_hold_time):
        dist_per_time = button_hold_time
        dist = dist_per_time * (cur_time_limit - button_hold_time)
        return dist

    probability = []
    for race_i in range(len(time)):
        cur_time_limit = time[race_i]
        cur_dist_record = distance[race_i]
        how_many_can_beat = 0
        for num_secs in range(cur_time_limit + 1):
            if dist_for_button_held(num_secs) > cur_dist_record:
                how_many_can_beat += 1
        probability.append(how_many_can_beat)

    if probability == []:
        return 0

    prob = 1
    for p in probability:
        prob *= p

    return prob





print(solution("2023//d6p1_input_ex.txt"))
print(solution("2023//d6p1_input.txt"))
