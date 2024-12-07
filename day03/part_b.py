import re

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

total = 0

res = [re.findall(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)', line) for line in input_lines]

do = True

for r in res:
  for w in r:
    if re.match(r'mul\(\d+,\d+\)', w) and do:
      [x,y] = re.findall(r'\d+', w)
      total += int(x) * int(y)
    if re.match(r'do\(\)', w):
      do = True
    elif re.match(r'don\'t\(\)', w):
      do = False

print('Part 2: {}'.format(total))
