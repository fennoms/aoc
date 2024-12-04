with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
s = 1
for slope in slopes:
    trees = 0
    x, y = 0, 0
    while x < len(lines) and y < len(lines[0]):
        if lines[x][y] == '#':
            trees += 1
        x += slope[1]
        y += slope[0]
        y %= len(lines[0])

    s *= trees

print(s)