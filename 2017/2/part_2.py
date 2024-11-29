import re

with open('input.txt') as f:
    data = f.read().strip().splitlines()
    data = [list(map(int, re.findall(r'\d+', line))) for line in data]

s = 0
for line in data:
    for i, x in enumerate(line):
        for j, y in enumerate(line):
            if i != j and x % y == 0:
                s += x // y

print(s)
            