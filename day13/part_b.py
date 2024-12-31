import re

with open('input.txt', 'r') as file:
  claws = file.read().strip().split('\n\n')

tkns = 0
offset = 10000000000000

for claw in claws:
  x_1, y_1, x_2, y_2, x_prize, y_prize = [int(i) for i in re.findall(r'\d+', claw)]
  x_prize += offset
  y_prize += offset
  
# Cramer's Rule it (thx r/adventofcode)
  a = (x_prize * y_2 - y_prize * x_2) / (x_1 * y_2 - y_1 * x_2)
  b = (y_prize * x_1 - x_prize * y_1) / (x_1 * y_2 - y_1 * x_2)
  if a.is_integer() and b.is_integer():
    tkns += (3*a) + b

print('Part 2: {}'.format(int(tkns)))
