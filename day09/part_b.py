from itertools import groupby
from operator import itemgetter

with open('input.txt', 'r') as file:
  line = list(file.read().strip())

# Expand the list
disk = list()
id = 0
files = dict()

for i in range(len(line)):
    if i % 2 == 0:
        files[id] = int(line[i])
        disk.extend([id] * int(line[i]))
        id += 1
    else:
        disk.extend('.' * int(line[i]))

# Get all positions of blanks
blanks = [list(map(itemgetter(1), v)) for k, v in groupby(enumerate([i for i, t in enumerate(disk) if t == '.']), lambda x: x[0] - x[1])]

ks = list(reversed(files.keys()))

# Sort the disk
for blank in blanks:
    while len(blank) > 0:
        k = list(filter(lambda x: files[x] <= len(blank), ks))
        if len(k) < 1:
            break
        else:
            tkn = k[0]
            for i in blank[:files[tkn]]:
                disk[i] = tkn
                disk[len(disk) - disk[-1::-1].index(tkn) - 1] = '.'
                blank.remove(i)
            ks.remove(tkn)

# Perform the checksum
checksum = sum(i * disk[i] for i in range(len(disk)) if disk[i] != '.')

print('Part 2: {}'.format(checksum))
