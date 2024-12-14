import math

import numpy as np
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


    def get_cost2(self, w_error=False):
        Px, Py = self.Px, self.Py
        if w_error is True:
            Px += 10000000000000
            Py += 10000000000000
        A = np.array([[self.Ax, self.Bx], [self.Ay, self.By]])
        b = np.array([Px , Py])
        x = np.linalg.solve(A, b)
        i, j = x
        if not (abs(i - round(i)) < 0.001 and abs(j - round(j)) < 0.001):
            return 0
        cost = (round(i) * self.A_cost) + (round(j) * self.B_cost)
        return cost

    def get_cost(self):
        for a in range(self.coin_limit + 1):
            for b in range(self.coin_limit + 1):
                if (self.Bx * b + self.Ax * a, self.By * b + self.Ay * a) == (self.Px, self.Py):
                    cost = (a * self.A_cost) + (b * self.B_cost)
                    return cost
        return 0






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
        total += machine.get_cost2(w_error=False)
    return total

def solution_2(x):
    total = 0
    for machine in machines:
        total += machine.get_cost2(w_error=True)
    return total

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


    start = timer()
    machines = parse_input("puzzle_input//d13_input.txt")
    result_2 = solution_2(machines)
    end = timer()
    print( f"{( end - start ) * 1000}ms" )
    print(f'Solution2: {result_2}')
