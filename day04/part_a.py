from collections import defaultdict
import re

# Slight modification to answer on SO
def get_strings(input, func):
    groups = defaultdict(list)
    strs = []

    for y in range(len(input)):
        for x in range(len(input[y])):
            groups[func(x, y)].append(input[y][x])

    for group in groups:
        strs.append(''.join(list(groups[group])))

    return strs

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

# Get all the rows, columns and diagonals
groups = input_lines.copy()
groups.extend(get_strings(input_lines, lambda x, y: x))
groups.extend([s for s in get_strings(input_lines, lambda x, y: x + y) if len(s) >= 4])
groups.extend([s for s in get_strings(input_lines, lambda x, y: x - y) if len(s) >= 4])

res = 0

for group in groups:
    # Hacky way to handle doubled groups
    r = len(re.findall(r'XMASAMX|SAMXMAS', group))*2
    res += r
    group = group.replace('XMASAMX', 'X..S..X')
    group = group.replace('SAMXMAS', 'S..X..S')

    r = len(re.findall(r'(?<=SAM)X|X(?=(MAS))', group))
    res += r

print('Part 1: {}'.format(res))
