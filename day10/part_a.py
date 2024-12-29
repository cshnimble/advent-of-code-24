# every coord is (y,x)

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

def get_coords(G, t):
    coords = list()
    for y, x in enumerate(G):
        for i in range(len(x)):
          if x[i] == t:
            coords.append((y, i))
    return coords

with open('test.txt', 'r') as file:
  input_lines = [[int(x) for x in line.strip()] for line in file]

MIN_X = 0
MAX_X = len(input_lines[0])
MIN_Y= 0
MAX_Y = len(input_lines)

# Get all '0' coords
starts = get_coords(input_lines, 0)

scores = { i: 0 for i in starts}

for start in scores.keys():
  #  print(start)
  scores[start] += 1

print('Part 1: {}'.format(sum(scores.values())))

# should eq 36