with open('input.txt', 'r') as f:
    grid = f.read().splitlines()
    grid = [list(x) for x in grid]

def starting_position(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                return i, j


def loop(grid, x, y):
    direction = (-1, 0)
    seen = set((x, y, direction[0], direction[1]))

    while True:
        if not (0 <= x + direction[0] < len(grid) and 0 <= y + direction[1] < len(grid[0])):
            break

        if grid[x + direction[0]][y + direction[1]] == '#':
            direction = (direction[1], direction[0] * -1)
        else:
            x += direction[0]
            y += direction[1]
        if (x, y, direction[0], direction[1]) in seen:
            return True
        seen.add((x, y, direction[0], direction[1]))
    
    return False

(x, y) = starting_position(grid)
s = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in ["#", "^"]:
            continue
        grid[i][j] = '#'
        if loop(grid, x, y):
            s += 1
        grid[i][j] = '.'

print(s)