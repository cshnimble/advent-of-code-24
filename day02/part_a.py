def is_inc_dec(line):
  ranges = [j-i for i, j in zip(line[:-1], line[1:])]
  return True if all(i > 0 for i in ranges) or all(i < 0 for i in ranges) else False

def is_in_range(line):
  ranges = [abs(j-i) for i, j in zip(line[:-1], line[1:])]
  trim = [i for i in ranges if i < 1 or i > 3]
  return True if len(trim) == 0 else False

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

safe = 0

for line in input_lines:
  nums = [int(x) for x in line.split()]
  if(is_in_range(nums) and is_inc_dec(nums)):
    safe += 1

print('Part 1: {}'.format(safe))
