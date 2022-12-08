
class directory():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.folders = []
        self.size = 0

    def __repr__(self):
        return self.name

    def add_size(self, file):
        self.total_size += file.size

class file():
    def __init__(self, name, size, parent):
        self.name = name
        self.parent = parent
        self.size = size

    def __repr__(self):
        return str(f'{self.size} {self.name}')

infile = "real_input.txt"
with open(infile, 'r') as f:
    data = [x[:-1] for x in f.readlines()]
del f
del infile

main_dir = directory('/', None)
cur_dir = main_dir

i = 1
while i < len(data):
    cmnd = data[i]
    if cmnd == '$ cd ..': # go to parent
        cur_dir = cur_dir.parent
        i += 1
    elif cmnd[:4] == '$ cd':
        go_where = cmnd[5:]
        for folder in cur_dir.folders:
            if folder.name == go_where:
                cur_dir = folder
                break
        i += 1
    elif cmnd[:4] == '$ ls':
        i += 1
        while i < len(data) and data[i][0] != '$':
            ls = data[i]
            if ls[:4] == 'dir ':
                cur_dir.folders.append(directory(ls[4:], cur_dir))
            else:
                this_file = ls.split(' ')
                size = int(this_file[0])
                name = this_file[1]
                cur_dir.files.append(file(name, size, cur_dir))
            i += 1

# print(main_dir)

# do dfs
def update_folder_size(the_dir):
    for folder in the_dir.folders:
        update_folder_size(folder)
        the_dir.size += folder.size
    for file in the_dir.files:
        the_dir.size += file.size

def get_folders_of_size_limit(the_dir, limit):
    def helper(cur_dir):
        for folder in cur_dir.folders:
            helper(folder)
            if folder.size <= limit:
                results.append(folder)
    results = []
    helper(the_dir)
    return results





update_folder_size(main_dir)
results = get_folders_of_size_limit(main_dir, 100000)
print(results)
cur_sum = 0
for folder in results:
    cur_sum += folder.size

print(cur_sum)
