with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

slope = (3, 1)
x, y = 0, 0
trees = 0

while x < len(lines) and y < len(lines[0]):
    if lines[x][y] == '#':
        trees += 1
    x += slope[1]
    y += slope[0]
    y %= len(lines[0])

print(trees)