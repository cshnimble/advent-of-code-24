import itertools

with open('input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

rules = input_lines[:input_lines.index('')]
updates = input_lines[input_lines.index('') +1:]

# Check if reverse of pair is not in rules, therefore invalid
def is_valid(x):
    if '{}|{}'.format(x[0],x[1]) in rules:
        return True
    elif '{}|{}'.format(x[1],x[0]) in rules:
        return False
    # Not in the list either way so ignore
    else:
        return True

# Takes a list of numbers, a list of swaps that need to happen and iterates
def fix_update_order(nums, swaps):
    for swap in swaps:
        i,j = nums.index(swap[0]), nums.index(swap[1])
        nums[i], nums[j] = nums[j], nums[i]
    return nums

res = 0

# Get all combos for updates and check reverse not in rules
for update in updates:
    nums = update.split(',')
    r = list(itertools.combinations(nums, 2))
    take = False
    swaps = []
    for x in r:
        if not is_valid(x):
            take = True
            swaps.append(x)
# If we're taking this one, fix the order and take the middle val
    if take:
        fixed = False
        while not fixed:
            fix = fix_update_order(nums, swaps)
            r = list(itertools.combinations(fix, 2))
            swaps = []
            fixed = True
            for x in r:
                if not is_valid(x):
                    fixed = False
                    swaps.append(x)
        res += int(fix[(len(fix) - 1)//2])

print('Part 2: {}'.format(res))
