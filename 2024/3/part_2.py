import re

with open('input.txt', 'r') as f:
    data = f.read().strip()

muls = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
enabled = True

s = 0
for x in muls:
    if x == "do()":
        enabled = True
    elif x == "don't()":
        enabled = False
    else:
        if not enabled:
            continue

        x, y = x[4:-1].split(',')
        s += int(x) * int(y)

print(s)
