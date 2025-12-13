import time


FNAME = "2025/puzzle_input/d12p1_example.txt"
FNAME = "2025/puzzle_input/d12p1_input.txt"

class Shape:
    def __init__(self, grid, mass):
        self.grid = grid
        self.mass = mass

    def __repr__(self):
        return '\n'.join([r for r in self.grid])

class Area:
    def __init__(self, w, l, shape_counts):
        self.w = w
        self.l = l
        self.shape_counts = shape_counts

def is_valid(a):
    area_total = a.w * a.l
    # easy win, area bigger than worst pack
    if area_total > sum(a.shape_counts) * 9:
        return True

    mass = 0
    for i, nshapes in enumerate(a.shape_counts):
        mass += nshapes * shapes[i].mass
    if area_total > mass:
        return True

    return False


def read():
    for_shapes = []
    for_areas = []
    with open(FNAME, 'r', encoding="UTF-8") as f:
        # get shapes
        for _ in range(6):
            grid = []
            mass = 0
            for _ in range(5):
                row = f.readline()[:-1]
                grid.append(row)
                mass += row.count('#')
            s = Shape(grid[1:-1], mass)
            for_shapes.append(s)

        for line in f:
            wl, shape_counts = line.split(": ")
            w, l = map(int, wl.split("x"))
            if w < l:
                w, l = l, w
            shape_counts = list(map(int, shape_counts[:-1].split(" ")))
            a = Area(w, l, shape_counts)
            for_areas.append(a)

    return for_shapes, for_areas

shapes, areas = read()
print(len(areas))
areas.sort(key=lambda x: (x.w, x.l, x.shape_counts) )

valid_counts = 0
for a in areas:
    # print(f"{a.w}x{a.l} : {a.shape_counts}")
    if is_valid(a):
        valid_counts += 1
print(valid_counts)

if "example" in FNAME:
    print("\nEXAMPLE")
    start_time = time.perf_counter()
    # print(f" == 2 {svr_to_out_with_fft_and_dac() == 2}")
    end_time = time.perf_counter()
    print(f"execution time: {(end_time - start_time):.6f}")
else:
    print("\nREAL")
    start_time = time.perf_counter()
    # print(f" == 473741288064360 {svr_to_out_with_fft_and_dac() == 473741288064360}")
    end_time = time.perf_counter()
    print(f"execution time: {(end_time - start_time):.6f}")

    print("\nways_to_reach: REAL")
    start_time = time.perf_counter()
    # print(f" == 473741288064360 {solve() == 473741288064360}")
    end_time = time.perf_counter()
    print(f"execution time: {(end_time - start_time):.6f}")
