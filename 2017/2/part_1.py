import re

with open('input.txt') as f:
    data = f.read().strip().splitlines()
    data = [list(map(int, re.findall(r'\d+', line))) for line in data]

s = 0
for line in data:
    mn = min(line)
    mx = max(line)
    s += mx - mn

print(s)