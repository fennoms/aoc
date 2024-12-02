with open('input.txt') as f:
    data = f.read().splitlines()
    data = list(map(int, data))

data.sort()

for i in range(len(data)):
    l = i + 1
    r = len(data) - 1
    while l < r:
        total = data[l] + data[r] + data[i]
        if total == 2020:
            print(data[l] * data[r] * data[i])
            break

        if total < 2020:
            l += 1
        else:
            r -= 1
