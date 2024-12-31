import re

with open('input.txt', 'r') as file:
  claws = file.read().strip().split('\n\n')

tkns = 0

for claw in claws:
  x_1, y_1, x_2, y_2, x_prize, y_prize = [int(i) for i in re.findall(r'\d+', claw)]
# Cramer's Rule it (thx r/adventofcode)
  a = (x_prize * y_2 - y_prize * x_2) / (x_1 * y_2 - y_1 * x_2)
  b = (y_prize * x_1 - x_prize * y_1) / (x_1 * y_2 - y_1 * x_2)
  if a.is_integer() and b.is_integer():
    tkns += (3*a) + b

print('Part 1: {}'.format(int(tkns)))
