import re
import itertools

def distance_between(a,b):
    return (a[0]-b[0], a[1]-b[1])

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

MIN_X = MIN_Y = 0
MAX_X = len(input_lines[0]) -1
MAX_Y = len(input_lines) -1

# Get all antenna types and locs
antenna_types = dict()
y = 0
for line in input_lines:
    types = (list(re.findall(r'\w', line)))
    if not len(types) == 0:
        for t in types:
            posns = [i for i,ch in enumerate(line) if ch == t]
            if t in antenna_types.keys():
                antenna_types[t].extend([(y, x) for x in posns])
            else:
                antenna_types[t] = [(y, x) for x in posns]
    y += 1

antinodes = set()

# Go through all pairs and add the antinodes to the set
for a in antenna_types.keys():
    pairs = list(itertools.combinations(antenna_types[a], 2))
    for pair in pairs:
        d = distance_between(pair[0],pair[1])
        antinodes.update([
                (pair[0][0] + d[0], pair[0][1] + d[1]),
                (pair[1][0] - d[0], pair[1][1] - d[1])
            ])

# Filter any out of bounds
locs = len(list(filter(lambda x:  MIN_Y <= x[0] <= MAX_Y and MIN_X <= x[1] <= MAX_X, antinodes)))

print('Part 1: {}'.format(locs))
