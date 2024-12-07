with open('input.txt', 'r') as file:
  input_lines = [list(line.strip()) for line in file]

# Limits
MIN_X = 0
MIN_Y = 0
MAX_X = len(input_lines[0]) - 1
MAX_Y = len(input_lines) - 1

# String possibilities
poss = ['MS MS', 'SM SM', 'MM SS', 'SS MM']

# Get positions of all As
coords = []

for i,j in enumerate(input_lines):
    for x in enumerate(j):
        if j[x[0]] == 'A':
            coords.append((i,x[0]))

res = 0

# Check the A can have 4 neighbours and that they're one of the possibilities
for (x,y) in coords:
    if MIN_X < x < MAX_X and MIN_Y < y < MAX_Y:
        cross = '{}{} {}{}'.format(input_lines[x-1][y-1], input_lines[x+1][y-1], input_lines[x-1][y+1], input_lines[x+1][y+1])
        if cross in poss:
            res += 1

print('Part 2: {}'.format(res))
