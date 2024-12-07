import re

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

total = 0

res = [re.findall(r'(mul\(\d+,\d+\))', line) for line in input_lines]

for r in res:
    for w in r:
        [x,y] = re.findall(r'\d+', w)
        total += int(x) * int(y)

print('Part 1: {}'.format(total))
