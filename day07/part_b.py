import re
import itertools
from functools import reduce
from operator import mul

# Performs Reverse Polish Notation to generate the total
def rpn(vals, ops):
    tot = 0
    while len(vals) > 1:
        a,b = vals.pop(0), vals.pop(0)
        op = ops.pop(0)
        if op == '||':
            tot = int('{}{}'.format(a,b))
        else:
            tot = eval('{} {} {}'.format(a,op,b))
        vals.insert(0, tot)
    return tot

with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

# Operands
ops = ['+', '*', '||']

# Final result tracker
tcr = 0

for line in input_lines:
    vals = re.findall(r'\d+', line)
    goal = int(vals[0])
    nums = [int(x) for x in vals[1:]]
    valid = False

# Total slots for insertions
    slots = len(nums) - 1
# Create all possible combos
    combos = [list(x) for x in itertools.product(ops, repeat=slots)]
# Do all the basic combos first
    ez = False
    if reduce(mul, nums) == goal or int(''.join(str(x) for x in nums)) == goal or sum(nums) == goal:
        tcr += goal
        ez = True
    else:
        combos = list(filter(lambda x: x not in [['+'] * slots, ['*'] * slots,['||'] * slots], combos))
        
# Try all the combos til one works
    if not ez:
        for combo in combos:
            tot = rpn(nums.copy(), combo)
            if tot == goal:
                tcr += goal
# Found valid combo, no need to continue
                break

print('Part 2: {}'.format(tcr))
