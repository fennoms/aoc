with open('input.txt', 'r') as f:
    grid = f.read().splitlines()

def starting_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                return i, j


(x, y) = starting_position(grid)

seen = set((x, y))
direction = (-1, 0)

while True:
    if not (0 <= x + direction[0] < len(grid) and 0 <= y + direction[1] < len(grid[0])):
        break

    if grid[x + direction[0]][y + direction[1]] == '#':
        direction = (direction[1], direction[0] * -1)

    x += direction[0]
    y += direction[1]
    seen.add((x, y))

print(len(seen))