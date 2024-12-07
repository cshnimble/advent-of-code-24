with open('input.txt', 'r') as file:
  input_lines = [line.strip() for line in file]

a, b = map(list, zip(*(s.split() for s in input_lines)))

a = sorted([int(x) for x in a])
b = sorted([int(x) for x in b])

difs = 0

for i in range(len(a)):
  difs += abs(a[i] - b[i])

print(difs)