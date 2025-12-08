

def read_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        grid = []
        for line in f:
            grid.append([c for c in line[:-1]])
    return grid
