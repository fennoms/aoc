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

# counter dict for l2
c = {}
for i in l2:
    c[i] = c.get(i, 0) + 1

s = 0
for i in range(len(l1)):
    s += (l1[i] * c.get(l1[i], 0))

print(s)