import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)

def get_coord(G, t):
    for y, x in enumerate(G):
        if t in x:
            return (y, x.index(t))

with open('input.txt', 'r') as file:
    input_lines = [list(line.strip()) for line in file]

# Map boundaries
MIN_X = 0
MIN_Y = 0
MAX_X = len(input_lines[0]) - 1
MAX_Y = len(input_lines) - 1

# Get guard starting position
start_pos = get_coord(input_lines, '^')
logger.debug('Starting position: {}'.format(start_pos))

# Start a list of steps taken
steps = [start_pos]

# Set the pointer
cur_pos = start_pos
cur_dir = 'N'

# Whilst we aren't on the edge of the map, move
while MIN_X < cur_pos[1] < MAX_X and MIN_Y < cur_pos[0] < MAX_Y:
    logger.debug('Heading {}'.format(cur_dir))
    new_pos = cur_pos
    if cur_dir == 'N':
        tmp = list(range(cur_pos[0]))
        logger.debug('Range of values to check over: {}'.format(tmp))
        hit = False
        for i in reversed(tmp):
            if input_lines[i][cur_pos[1]] == '#':
                logger.debug('Collision detected at {}'.format((i,cur_pos[1])))
                new_pos = (i + 1, cur_pos[1])
                logger.debug('Moving to position {}'.format(new_pos))
                cur_dir = 'E'
                hit = True
                break
        if not hit:
            logger.debug('No collision detected, moving to edge of map')
            new_pos = (MIN_Y, cur_pos[1])
            logger.debug('Moving to position {}'.format(new_pos))
        steps.extend([(x, cur_pos[1]) for x in range(new_pos[0], cur_pos[0])])
        cur_pos = new_pos

    elif cur_dir == 'S':
        tmp = list(range(cur_pos[0], MAX_Y + 1))
        logger.debug('Range of values to check over: {}'.format(tmp))
        hit = False
        for i in tmp:
            if input_lines[i][cur_pos[1]] == '#':
                logger.debug('Collision detected at {}'.format((i,cur_pos[1])))
                new_pos = (i - 1, cur_pos[1])
                logger.debug('Moving to position {}'.format(new_pos))
                cur_dir = 'W'
                hit = True
                break
        if not hit:
            logger.debug('No collision detected, moving to edge of map')
            new_pos = (MAX_Y, cur_pos[1])
            logger.debug('Moving to position {}'.format(new_pos))
        steps.extend([(x, cur_pos[1]) for x in range(cur_pos[0], new_pos[0] + 1)])
        cur_pos = new_pos

    elif cur_dir == 'E':
        tmp = list(range(cur_pos[1], MAX_X + 1))
        logger.debug('Range of values to check over: {}'.format(tmp))
        hit = False
        for i in tmp:
            if input_lines[cur_pos[0]][i] == '#':
                logger.debug('Collision detected at {}'.format((i,cur_pos[1])))
                new_pos = (cur_pos[0], i - 1)
                logger.debug('Moving to position {}'.format(new_pos))
                cur_dir = 'S'
                hit = True
                break
        if not hit:
            logger.debug('No collision detected, moving to edge of map')
            new_pos = (cur_pos[0], MAX_X)
            logger.debug('Moving to position {}'.format(new_pos))
        steps.extend([(cur_pos[0], x) for x in range(cur_pos[1], new_pos[1] + 1)])
        cur_pos = new_pos

    elif cur_dir == 'W':
        tmp = list(range(cur_pos[1]))
        logger.debug('Range of values to check over: {}'.format(tmp))
        hit = False
        for i in reversed(tmp):
            if input_lines[cur_pos[0]][i] == '#':
                logger.debug('Collision detected at {}'.format((i,cur_pos[1])))
                new_pos = (cur_pos[0], i + 1)
                logger.debug('Moving to position {}'.format(new_pos))
                cur_dir = 'N'
                hit = True
                break
        if not hit:
            logger.debug('No collision detected, moving to edge of map')
            new_pos = (cur_pos[0], MIN_X)
            logger.debug('Moving to position {}'.format(new_pos))
        steps.extend([(cur_pos[0], x) for x in range(new_pos[1], cur_pos[1])])
        cur_pos = new_pos

logger.debug('Removing duplicate steps')
s1 = list(dict.fromkeys(steps))

res = len(s1)
logger.debug('Total steps after duplicate removal: {}'.format(res))

print('Part 1: {}'.format(res))
