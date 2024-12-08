ANTINODE = '#'
EMPTY = '.'

with open('input.txt', 'r') as f:
    grid = f.read().strip().splitlines()
    grid = [list(row) for row in grid]

def in_grid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

antennas = {}
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] not in [ANTINODE, EMPTY]:
            antennas[grid[x][y]] = antennas.get(grid[x][y], []) + [(x, y)]

# must use a set because we cant directly use the grid because
# nodes and antinodes may overlap
antinodes = set()

for a in antennas.values():
    for a1 in range(len(a)):
        for a2 in range(a1 + 1, len(a)):
            a1_x, a1_y = a[a1]
            a2_x, a2_y = a[a2]

            diff_x, diff_y = a2_x - a1_x, a2_y - a1_y

            if in_grid(grid, a1_x - diff_x, a1_y - diff_y):
                antinodes.add((a1_x - diff_x, a1_y - diff_y))
            
            if in_grid(grid, a2_x + diff_x, a2_y + diff_y):
                antinodes.add((a2_x + diff_x, a2_y + diff_y))

print(len(antinodes))
