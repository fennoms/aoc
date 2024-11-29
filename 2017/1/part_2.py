with open('input.txt', 'r') as f:
    data = list(f.read().strip())
    data = list(map(int, data))

half = len(data) // 2 # even list

s = 0
for i in range(len(data) - 1):
    idx = (i + half) % len(data)
    if data[i] == data[idx]:
        s += data[i]

print(s)