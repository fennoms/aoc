with open('input.txt', 'r') as f:
    data = list(f.read().strip())
    data = list(map(int, data))

s = 0
for i in range(len(data) - 1):
    if data[i] == data[i + 1]:
        s += data[i]

if data[-1] == data[0]:
    s += data[-1]

print(s)