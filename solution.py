class monkey():
    def __init__(self, monkey_num:str, items:list, operation:str, test:str, true_case:str, false_case:str):
        self.inspection_count = 0
        monkey_num = monkey_num.split(' ')
        self.monkey_num = int(monkey_num[-1])
        items = items.split(': ')
        items = items[-1]
        items = items.split(', ')
        self.items = [int(x) for x in items]
        #parse operation

        if operation[-9:] == 'old * old':
            self.operator = 'old * old'
        elif operation[-9:] == 'old + old':
            self.operator = 'old + old'
        else:
            operation = operation.split(' ')
            self.operation_val = int(operation[-1])
            self.operator = operation[-2]

        # parse test
        test = test.split(' ')
        self.test_val = int(test[-1])
        to_monkey_true = true_case.split(' ')
        self.to_monkey_true = int(to_monkey_true[-1])
        to_monkey_false = false_case.split(' ')
        self.to_monkey_false = int(to_monkey_false[-1])

    def operation(self, worry):
        if self.operator == 'old * old':
            return worry * worry
        if self.operator == 'old + old':
            return worry + worry
        if self.operator == '*':
                return worry * self.operation_val
        elif self.operator == '+':
            return worry + self.operation_val

    def test(self, worry):
        if worry % self.test_val == 0:
            return self.to_monkey_true
        return self.to_monkey_false

    def add_item(self, item):
        self.items.append(item)

    def inspect_items(self):
        to_pass = []
        for item in self.items:
            new_item = self.operation(item) # inspect / run operation
            # new_item = new_item // 3 # relief
            to_monkey = self.test(new_item)
            to_pass.append((new_item, to_monkey))
            self.inspection_count += 1
        self.items = []
        return to_pass



infile = "real_input.txt"
infile = "sample_input.txt"
monkeys = []
data = []
with open(infile, 'r') as f:
    for line in f:
        data.append(line[:-1])

for i in range(0, len(data), 7):
    monkey_num = data[i]
    items = data[i+1]
    operation = data[i+2]
    test = data[i+3]
    true_case = data[i+4]
    false_case = data[i+5]
    monkeys.append(monkey(monkey_num[:-1], items, operation, test, true_case, false_case))

for i in range(10000):
    for monkey in monkeys:
        to_pass = monkey.inspect_items()
        for new_item, to_monkey in to_pass:
            monkeys[to_monkey].add_item(new_item)
# print(monkeys)

counts = []
for monkey in monkeys:
    counts.append((monkey.inspection_count, monkey.monkey_num))

counts.sort()
print(counts)
print(counts[-1][0]*counts[-2][0])
