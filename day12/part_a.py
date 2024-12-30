with open('test2.txt', 'r') as file:
  grid = [line.strip() for line in file]

# find all uniques in the grid
region_types = dict()
for y,x in enumerate(grid):
  for r in x:
    if r in region_types.keys():
      region_types[r] +=1
    else:
      region_types[r] = 1

price = 0

print('Part 1: {}'.format(price))

# should eq 140