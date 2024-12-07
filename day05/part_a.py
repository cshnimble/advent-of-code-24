import itertools

with open('input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

rules = input_lines[:input_lines.index('')]
updates = input_lines[input_lines.index('') +1:]

res = 0

# Get all combos for updates and check reverse not in rules
for update in updates:
    nums = update.split(',')
    r = list(itertools.combinations(nums, 2))
    valid = True
    for x in r:
        if '{}|{}'.format(x[1],x[0]) in rules:
            valid = False

    if valid:
        res += int(nums[(len(nums) - 1)//2])

print('Part 1: {}'.format(res))
