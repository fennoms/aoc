with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    data = [x.split('  ') for x in data]

l1 = []
l2 = []

for x, y in data:
    l1.append(int(x))
    l2.append(int(y))

l1.sort()
l2.sort()

s = 0
for i in range(len(l1)):
    s += abs(l1[i] - l2[i])

print(s)