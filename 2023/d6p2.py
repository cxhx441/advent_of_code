def solution(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        time = f.readline()
        time = time[len("Time: "):-1]
        time = time.replace(" ", "")
        time = int(time)
        distance = f.readline()
        distance = distance[len("Distance: "):-1].replace(" ", "")
        distance = int(distance)

    def dist_for_button_held(button_hold_time):
        dist_per_time = button_hold_time
        dist = dist_per_time * (cur_time_limit - button_hold_time)
        return dist

    probability = []
    cur_time_limit = time
    cur_dist_record = distance
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





print(solution("2023//d6p2_input_ex.txt"))
print(solution("2023//d6p2_input.txt"))
