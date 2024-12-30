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

def update(stones):
  new = dict()
  for stone in stones.keys():
    new_stones = change(int(stone))
    for new_stone in new_stones:
      if new.get(new_stone) is None:
        new[new_stone] = 0
      new[new_stone] += stones[stone]
  return new

with open('input.txt', 'r') as file:
  stones = file.read().strip().split(' ')

count = { int(i): 1 for i in stones }

for _ in range(75):
  count = update(count)

print('Part 2: {}'.format(sum(count.values())))
