import re
import itertools

# Performs Reverse Polish Notation to generate the total
def rpn(vals, ops):
    sum = 0
    while len(vals) > 1:
        a,b = vals.pop(0), vals.pop(0)
        op = ops.pop(0)
        sum = eval('{} {} {}'.format(a,op,b))
        vals.insert(0, sum)
    return sum

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

# Operands
ops = ['+', '*']

# Final result tracker
tcr = 0

for line in input_lines:
    vals = re.findall(r'\d+', line)
    goal = int(vals[0])
    nums = vals[1:]
    valid = False

# Total slots for insertions
    slots = len(nums) - 1
# Create all possible combos
    combos = [list(x) for x in itertools.product(ops, repeat=slots)]
# Try all the combos til one works
    for combo in combos:
        sum = rpn(nums.copy(), combo)
        if sum == goal:
            valid = True
# Found valid combo, no need to continue
            break

# Add the goal to the tracker
    if valid:
        tcr += goal

print('Part 1: {}'.format(tcr))
