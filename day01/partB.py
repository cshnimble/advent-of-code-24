with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

a, b = map(list, zip(*(s.split() for s in input_lines)))

score = sum([int(x) * b.count(x) for x in a])

print(score)