with open('input.txt', 'r') as f:
    grid = f.read().splitlines()

type Grid = list[str]

def in_grid(grid: Grid, x: int, y: int) -> bool:
    return 0 <= y < len(grid) and 0 <= x < len(grid[y])

def right_sam_mas(grid: Grid, x: int, y: int) -> bool:
    dirs = [(1, 1), (-1, -1)]
    if not all(in_grid(grid, x + i, y + j) for i, j in dirs):
        return False
    
    return grid[x][y] == 'A' and ((grid[x + 1][y + 1] == 'S' and grid[x - 1][y - 1] == 'M') or (grid[x + 1][y + 1] == 'M' and grid[x - 1][y - 1] == 'S'))


def left_sam_mas(grid: Grid, x: int, y: int) -> bool:
    dirs = [(1, -1), (-1, 1)]
    if not all(in_grid(grid, x + i, y + j) for i, j in dirs):
        return False
    
    return grid[x][y] == 'A' and ((grid[x + 1][y - 1] == 'S' and grid[x - 1][y + 1] == 'M') or (grid[x + 1][y - 1] == 'M' and grid[x - 1][y + 1] == 'S'))

s = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] != 'A':
            continue

        if right_sam_mas(grid, x, y) and left_sam_mas(grid, x, y):
            s += 1


print(s)
