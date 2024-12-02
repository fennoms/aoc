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
        # at least one, at most three
        if abs(data[i] - data[i - 1]) > 3 or abs(data[i] - data[i - 1]) < 1:
            return False
    return True


with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    data = [list(map(int, x.split(' '))) for x in data]

s = 0
for x in data:
    if all_increasing(x) or all_decreasing(x):
        if gradually_increasing_decreasing(x):
            s += 1

print(s)