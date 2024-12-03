import re

with open('input.txt', 'r') as f:
    data = f.read().strip()

muls = re.findall(r"mul\(\d+,\d+\)", data)

muls = [x[4:-1].split(',') for x in muls]

s = 0
for x, y in muls:
    s += int(x) * int(y)

print(s)
