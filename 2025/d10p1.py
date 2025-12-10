
class Machine:
    def __init__(self):
        self.machine_n = 0
        self.lights = 0
        self.nlights = 0
        self.lights_req = 0
        self.buttons = []
        self.joltage_req = None

    def __str__(self):
        s = []
        s.append(f"Machine:    #{self.machine_n}")
        s.append(f"Lights req: {self.lights_req:0{self.nlights}b}")
        s.append(f"Lights    : {self.lights:0{self.nlights}b}")
        buttonstr = ', '.join([f"{but:0{self.nlights}b}" for but in self.buttons])
        s.append(f"Buttons   : {buttonstr}")

        return '\n'.join(s)

    def execute(self, button_order):
        lights = 0
        for i in button_order:
            lights ^= self.buttons[i]
        return lights

    def brute_force_powerset_solve(self):
        min_button_presses = float("inf")
        n = len(self.buttons)

        def helper(start, path):
            nonlocal min_button_presses
            if start == n:
                # print(path)
                if self.execute(path) == self.lights_req and len(path) < min_button_presses:
                    min_button_presses = len(path)
                return

            helper(start + 1, path + [start])
            helper(start + 1, path)

        helper(0, [])
        return min_button_presses


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
                bmask = 0
                for num in b:
                    bmask += 1 << (m.nlights - num - 1)
                m.buttons.append(bmask)
            machines.append(m)
    return machines


machines = read()
result = 0
for m in machines:
    result += m.brute_force_powerset_solve()
print(result)
