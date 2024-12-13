import math
from timeit import default_timer as timer
class Machine:
    def __init__(self, Ax, Ay, Bx, By, Px, Py):
        self.Ax = Ax
        self.Ay = Ay
        self.Bx = Bx
        self.By = By
        self.Px = Px
        self.Py = Py
        self.A_cost = 3
        self.B_cost = 1
        self.coin_limit = 100

    def _calc_cost(self, a, b):
        return (a * self.A_cost) + (b * self.B_cost)

    def get_cost(self):
        for a in range(self.coin_limit + 1):
            for b in range(self.coin_limit + 1):
                if (self.Bx * b + self.Ax * a, self.By * b + self.Ay * a) == (self.Px, self.Py):
                    cost = (a * self.A_cost) + (b * self.B_cost)
                    return cost
        return 0

    def get_cost2(self):
        self.Px += 10000000000000
        self.Py += 10000000000000
        determ = self.Ax * self.By - self.Bx * self.Ay
        if any([determ == 0, a_num % self.d != 0, b_num % self.d != 0]):
            return 0
        # TODO linear equation solver?





def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        machines = []
        Ax = Ay = Bx = By = Px = Py = None
        for line in f:
            if line == '\n':
                continue
            if line.startswith('Button A:'):
                x = line.find('X')
                comma = line.find(',')
                Ax = int(line[x+2: comma])

                y = line.find('Y')
                Ay = int(line[y+2: -1])

            elif line.startswith('Button B:'):
                x = line.find('X')
                comma = line.find(',')
                Bx = int(line[x+2: comma])

                y = line.find('Y')
                By = int(line[y+2: -1])

            elif line.startswith('Prize:'):
                x = line.find('X')
                comma = line.find(',')
                Px = int(line[x+2: comma])

                y = line.find('Y')
                Py = int(line[y+2: -1])
                machines.append(Machine(Ax, Ay, Bx, By, Px, Py))
    return machines

def solution_1(machines):
    total = 0
    for machine in machines:
        total += machine.get_cost()
    return total

def solution_2(x):
    return 0

if __name__ == "__main__":
    start = timer()
    machines = parse_input("puzzle_input//d13_input.txt")
    result = solution_1(machines)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution1: {result}')

    # start = timer()
    # machines = parse_input("puzzle_input//d13_input_ex3.txt")
    # result = solution_1(machines)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution1: {result}')


    # start = timer()
    # input = parse_input("puzzle_input//d#_input.txt")
    # result_2 = solution_2(input)
    # end = timer()
    # print( f"{( end - start ) * 1000}ms" )
    # print(f'Solution2: {result}')
