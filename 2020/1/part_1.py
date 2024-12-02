with open('input.txt') as f:
    data = f.read().splitlines()
    data = list(map(int, data))

data.sort()
l = 0
r = len(data) - 1


while l < r:
    total = data[l] + data[r]
    if total == 2020:
        print(data[l] * data[r])
        break

    if total < 2020:
        l += 1
    else:
        r -= 1
