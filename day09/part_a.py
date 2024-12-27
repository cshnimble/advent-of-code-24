with open('input.txt', 'r') as file:
  line = list(file.read().strip())

# Expand the list
disk = list()
id = 0

for i in range(len(line)):
    if i % 2 == 0:
        disk.extend([id] * int(line[i]))
        id += 1
    else:
        disk.extend('.' * int(line[i]))

# Sort the disk
for i in reversed(range(len(disk))):
    if disk[i] != '.':
        if(disk.index('.') < i):
            s = disk.index('.')
            disk[s], disk[i] = disk[i], disk[s]
        else:
            break

# Perform the checksum
checksum = sum(i * disk[i] for i in range(len(disk)) if disk[i] != '.')

print('Part 1: {}'.format(checksum))
