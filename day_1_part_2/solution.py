# from collections import heapq
import heapq
def input_to_list(infile):
    data = []
    with open(infile, 'r') as f:
        for line in f:
            line = line [:-1]
            if line:
                data.append(int(line))
            else:
                data.append(line)
    data.append('')
    return data

data = input_to_list("sample_input.txt") # 45000
data = input_to_list("real_input.txt") #

calorie_sum = 0
max_food_calories = 0
heap = []
for food in data:
    if food != '':
        calorie_sum += food
    else:
        heapq.heappush(heap, -calorie_sum) # for max heap
        calorie_sum = 0

# final sum
print(heap)
final = 0
final -= heapq.heappop(heap)
final -= heapq.heappop(heap)
final -= heapq.heappop(heap)

print(final)
