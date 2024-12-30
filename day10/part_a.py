import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

def get_coords(G, t):
    coords = list()
    for y, x in enumerate(G):
        if t in x:
            coords.append((y, x.index(t)))
    return coords

with open('test.txt', 'r') as file:
  input_lines = [[int(x) for x in line.strip()] for line in file]

# Get all '9' coords
nines = get_coords(input_lines, 9)


scores = 0

print('Part 1: {}'.format(scores))