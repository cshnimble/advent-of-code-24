def change(stone):
  res = list()
  if stone == 0:
    res.append(1)
  elif len(str(stone)) % 2 == 0:
    tmp = str(stone)
    res.extend([int(tmp[:len(tmp)//2]), int(tmp[len(tmp)//2:])])
  else:
    res.append(stone * 2024)
  return res

with open('input.txt', 'r') as file:
  stones = file.read().strip().split(' ')

for i in range(25):
  new = list()
  while len(stones) > 0:
    new.extend(change(int(stones.pop(0))))
  stones = new

count = len(stones)

print('Part 1: {}'.format(count))
