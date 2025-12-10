import collections
import numpy as np
import scipy.optimize as optim
import z3
# from z3 import *

class Machine:
    def __init__(self):
        self.machine_n = 0
        self.lights = 0
        self.nlights = 0
        self.lights_req = 0
        self.buttons = []
        self.joltage_req = None
        self.joltage = None

    def __str__(self):
        s = []
        s.append(f"Machine:    #{self.machine_n}")
        s.append(f"Joltage req: {self.joltage_req}")
        s.append(f"Joltage    : {self.joltage}")
        # buttonstr = ', '.join([f"{but:0{self.nlights}b}" for but in self.buttons])
        # s.append(f"Buttons   : {buttonstr}")
        s.append(f"Buttons    : {self.buttons}")

        return '\n'.join(s)

    def execute(self, button_order):
        lights = 0
        for i in button_order:
            lights ^= self.buttons[i]
        return lights

    # def matrix_solve(self):
    #     a = []
    #     for button in self.buttons:
    #         row = [0] * len(self.joltage)
    #         for i in button:
    #             row[i] = 1
    #         a.append(row)
    #     b = self.joltage_req
    #     try:
    #         x = np.linalg.solve(a, b)
    #         print("success")
    #         print(f"x: {x}")
    #     except np.linalg.LinAlgError as e:
    #         print(f"error {e}")
    #         x = -1
    #     # print(x)
    #     return x
    def solve_z3(self):
        nb = []
        for b in self.buttons:
            row = [0] * len(self.joltage)
            for i in b:
                row[i] = 1
            nb.append(row)

        variables = [0] * len(self.buttons)
        s = z3.Solver()
        for i in range(len(variables)):
            s.add( sum( [ variables[i] * nb[r][i] for r in range(len(self.buttons)) ] ) == self.joltage_req[i])
            s.add( variables[i] >= 0 )
        return 0

    def solve_scipy(self):
        # this solution works.
        min_presses = 0
        joltage = np.asarray(self.joltage_req)
        nb = []
        for b in self.buttons:
            row = [0] * len(self.joltage)
            for i in b:
                row[i] = 1
            nb.append(row)
        buttons = np.asarray(nb)
        c = np.asarray([1]*len(self.buttons))
        buttonst = buttons.transpose()
        opt = optim.linprog(c, A_eq=buttonst,b_eq = joltage,integrality=1)
        num_presses = opt.fun
        # if opt.status != 0:
        #     print("HOUSTON WE HAVE A i"PROBLEM")
        #     print(f"The problem is:{opt.status}")
        #     print(joltage)
        #     print(opt.fun)
        #     print(buttonst)
        #     print(opt)

        #print(f"The fewest buttons needed to be pressed was {num_presses}")
        min_presses += num_presses
        # print(f"The total number of buttons that need to be pressed is {tot_few_butt}")
        return min_presses

    def solve(self):
        mp = collections.defaultdict(list)
        for button in self.buttons:
            for b in button:
                mp[b].append(button)

        joltage = self.joltage_req.copy()
        min_push = float("inf")
        def helper(cur, pushn):
            nonlocal min_push
            for j in joltage:
                if j < 0:
                    return

            if joltage == [0] * len(joltage):
                min_push = min(min_push, pushn)
                return
            if cur >= len(self.buttons):
                return

            # n = len(mp[cur])
            for b in mp[cur]:
                jc = joltage[cur]
                for jolt in range(jc):
                    for i in b: joltage[i] -= 1 * (jc - jolt)
                    if joltage[cur] == 0:
                        helper(cur+1, pushn + (jc-jolt))
                    elif joltage[cur] > 0:
                        helper(cur, pushn + (jc-jolt))
                    for i in b: joltage[i] += 1 * (jc - jolt)

        helper(0, 0)
        return min_push

fname = "2025/puzzle_input/d10p1_example.txt"
fname = "2025/puzzle_input/d10p1_input.txt"
def read():
    machines = []
    machine_num = 0
    with open(fname, 'r', encoding="UTF-8") as f:
        for line in f:
            m = Machine()
            m.machine_n = machine_num
            machine_num += 1
            split = line[:-1].split(' ')
            m.joltage_req = [int(j) for j in split[-1][1:-1].split(',')]
            m.joltage = [ 0 for _ in range(len(m.joltage_req))]

            lights_req = split[0]
            lights_req = lights_req[1:-1]
            m.nlights = len(lights_req)
            lights_req_bin = 0
            for l in lights_req:
                lights_req_bin = lights_req_bin << 1
                if l == "#":
                    lights_req_bin += 1
            m.lights_req = lights_req_bin

            buttons = split[1:-1]
            for b in buttons:
                b = b[1:-1]
                b = b.split(",")
                b = [ int(x) for x in b ]
                # bmask = 0
                # for num in b:
                #     bmask += 1 << (m.nlights - num - 1)
                m.buttons.append(b)
            machines.append(m)
    return machines

machines = read()
result = 0
for m in machines:
    # result += m.brute_force_powerset_solve()
    print()
    print(m)
    tmp = m.solve_z3()
    print(tmp)
    result += tmp
print(result)
