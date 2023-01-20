def input_to_list(infile):
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line [:-1]
            if line:
                data.append(int(line))
            else:
                data.append(line)
    return data

data = input_to_list("sample_input.txt") # 24000
data = input_to_list("real_input.txt")  # 69177

calorie_sum = 0
max_food_calories = 0
for food in data:
    if food != '':
        calorie_sum += food
    else:
        max_food_calories = max(max_food_calories, calorie_sum)
        calorie_sum = 0

print(max_food_calories)
