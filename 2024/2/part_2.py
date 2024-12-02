def all_increasing(data: list[int]) -> bool:
    for i in range(1, len(data)):
        if data[i] < data[i - 1]:
            return False
    return True

def all_decreasing(data: list[int]) -> bool:
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            return False
    return True
        
def gradually_increasing_decreasing(data: list[int]) -> bool:
    for i in range(1, len(data)):
        if abs(data[i] - data[i - 1]) > 3 or abs(data[i] - data[i - 1]) < 1:
            return False
    return True


with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    data = [list(map(int, x.split(' '))) for x in data]

s = 0
for x in data:
    safe = False
    if all_increasing(x) or all_decreasing(x):
        if gradually_increasing_decreasing(x):
            s += 1
            safe = True

    if not safe:
        for i in range(len(x)):
            y = x.pop(i)
            if all_increasing(x) or all_decreasing(x):
                if gradually_increasing_decreasing(x):
                    s += 1
                    break
            x.insert(i, y)

print(s)
