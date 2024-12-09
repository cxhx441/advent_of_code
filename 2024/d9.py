from timeit import default_timer as timer
import collections

def parse_input(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            diskmap = [ int(num) for num in line[:-1] ]
    return diskmap

def solution_1(diskmap):
    def expand(diskmap):
        expansion = []
        i = 0
        filenum = 0
        while i < len(diskmap) - 1:
            filespace = diskmap[i]
            freespace = diskmap[i + 1]
            for _ in range(filespace):
                expansion.append(filenum)
            for _ in range(freespace):
                expansion.append(None)
            i += 2
            filenum += 1

        filespace = diskmap[i]
        for _ in range(filespace):
            expansion.append(filenum)
        return expansion

    def compress(data):
        l, r = 0, len(data) - 1
        while l < r:
            if data[l] != None:
                l += 1
            elif data[r] == None:
                r -= 1
            else:
                data[l], data[r] = data[r], data[l]
        return data

    def checksum(data):
        total = 0
        for i, filenum in enumerate(data):
            if filenum is None:
                break
            total += i * filenum
        return total

    expansion = expand(diskmap)
    compressed = compress(expansion.copy())

    return checksum(compressed)

# diskmap = parse_input("2024//puzzle_input//d9_input_ex.txt")
# result_1 = solution_1(diskmap)
# print(result_1)
# assert result_1 == 1928

# start = timer()
# diskmap = parse_input("2024//puzzle_input//d9_input.txt")
# result = solution_1(diskmap)
# print(result)
# end = timer()
# print( f"{( end - start ) * 1000}ms" )
# print(result)





def solution_2(diskmap):
    def expand(diskmap):
        expansion = []
        i = 0
        filenum = 0
        while i < len(diskmap) - 1:
            filespace = diskmap[i]
            freespace = diskmap[i + 1]
            for _ in range(filespace):
                expansion.append(filenum)
            for _ in range(freespace):
                expansion.append(None)
            i += 2
            filenum += 1

        filespace = diskmap[i]
        for _ in range(filespace):
            expansion.append(filenum)
        return expansion

    def get_freespace_dict(diskmap):
        freespace_mp = list()
        freespace_begin_location = 0
        i = 0
        while i < len(diskmap) - 1:
            freespace_begin_location += diskmap[i]
            size = diskmap[i + 1]
            if size != 0:
                freespace_mp.append( (freespace_begin_location, size) )
            freespace_begin_location += diskmap[i + 1]
            i += 2

        # freespace_begin_location = 0
        # i = 0
        # while i < len(diskmap) - 1:
        #     freespace_begin_location += diskmap[i]
        #     size = diskmap[i + 1]
        #     freespace_dict[size].append(freespace_begin_location)
        #     freespace_begin_location += diskmap[i + 1]
        #     i += 2

        # for size, locations in freespace_dict.items():
        #     locations.reverse()

        return freespace_mp

    def compress(data):
        r = len(data) - 1

        while r >= 0:
            while r >= 0 and data[r] is None:
                r -= 1
            # filenum = data[r]
            start = end = r
            while data[start - 1] == data[end]:
                start -= 1
            blocksize = end - start + 1

            for mp_i, (loc, freespace) in enumerate(freespace_mp):
                if loc >= start:
                    break
                if freespace < blocksize:
                    continue

                lw = loc
                rw = start
                for i in range(blocksize):
                    data[lw + i], data[rw + i] = data[rw + i], data[lw + i]
                    # l += 1
                    # start += 1

                freespace_mp[mp_i] = (loc + blocksize, freespace - blocksize)
                break
            # r -= blocksize
            r -= blocksize

        return data

    def checksum(data):
        total = 0
        for i, filenum in enumerate(data):
            if filenum is None:
                continue
            total += i * filenum
        return total

    freespace_mp = get_freespace_dict(diskmap)
    expansion = expand(diskmap)
    print(''.join([ str(x) if x is not None else '.' for x in expansion]))
    compressed = compress(expansion.copy())

    return checksum(compressed)

diskmap = parse_input("2024//puzzle_input//d9_input_ex.txt")
result_2 = solution_2(diskmap)
print(result_2)
assert result_2 == 2858

start = timer()
input = parse_input("2024//puzzle_input//d9_input.txt")
result_2 = solution_2(input)
print(result_2)
end = timer()
print( f"{( end - start ) * 1000}ms" )
print(result_2)

