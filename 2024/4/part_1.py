with open('input.txt', 'r') as f:
    grid = f.read().splitlines()

type Grid = list[str]

def in_grid(grid: Grid, x: int, y: int) -> bool:
    return 0 <= y < len(grid) and 0 <= x < len(grid[y])


def xmas_right(grid: Grid, x: int, y: int) -> bool:
    if not all(in_grid(grid, x + i, y) for i in range(4)):
        return False
    
    return grid[x][y] == 'X' and grid[x + 1][y] == 'M' and grid[x + 2][y] == 'A' and grid[x + 3][y] == 'S'


def xmas_left(grid: Grid, x: int, y: int) -> bool:
    if not all(in_grid(grid, x - i, y) for i in range(4)):
        return False
    
    return grid[x][y] == 'X' and grid[x - 1][y] == 'M' and grid[x - 2][y] == 'A' and grid[x - 3][y] == 'S'


def xmas_top(grid: Grid, x: int, y: int) -> bool:
    if not all(in_grid(grid, x, y - i) for i in range(4)):
        return False
    
    return grid[x][y] == 'X' and grid[x][y - 1] == 'M' and grid[x][y - 2] == 'A' and grid[x][y - 3] == 'S'


def xmas_bottom(grid: Grid, x: int, y: int) -> bool:
    if not all(in_grid(grid, x, y + i) for i in range(4)):
        return False
    
    return grid[x][y] == 'X' and grid[x][y + 1] == 'M' and grid[x][y + 2] == 'A' and grid[x][y + 3] == 'S'


def xmas_top_right(grid: Grid, x: int, y: int) -> bool:

    dirs = [(-1, 1), (-2, 2), (-3, 3)]
    if not all(in_grid(grid, x + i, y + j) for i, j in dirs):
        return False
    
    return grid[x][y] == 'X' and grid[x - 1][y + 1] == 'M' and grid[x - 2][y + 2] == 'A' and grid[x - 3][y + 3] == 'S'


def xmas_top_left(grid: Grid, x: int, y: int) -> bool:
    dirs = [(-1, -1), (-2,-2), (-3, -3)]
    if not all(in_grid(grid, x + i, y + j) for i, j in dirs):
        return False

    return grid[x][y] == 'X' and grid[x - 1][y - 1] == 'M' and grid[x - 2][y - 2] == 'A' and grid[x - 3][y - 3] == 'S'


def xmas_bottom_right(grid: Grid, x: int, y: int) -> bool:
    dirs = [(1, 1), (2, 2), (3, 3)]
    if not all(in_grid(grid, x + i, y + j) for i, j in dirs):
        return False

    return grid[x][y] == 'X' and grid[x + 1][y + 1] == 'M' and grid[x + 2][y + 2] == 'A' and grid[x + 3][y + 3] == 'S'


def xmas_bottom_left(grid: Grid, x: int, y: int) -> bool:
    dirs = [(1, -1), (2, -2), (3, -3)]
    if not all(in_grid(grid, x + i, y + j) for i, j in dirs):
        return False

    return grid[x][y] == 'X' and grid[x + 1][y - 1] == 'M' and grid[x + 2][y - 2] == 'A' and grid[x + 3][y - 3] == 'S'


s = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] != 'X':
            continue

        s += (
            int(xmas_right(grid, x, y)) +
            int(xmas_left(grid, x, y)) +
            int(xmas_top(grid, x, y)) +
            int(xmas_bottom(grid, x, y)) +
            int(xmas_top_right(grid, x, y)) +
            int(xmas_top_left(grid, x, y)) +
            int(xmas_bottom_right(grid, x, y)) +
            int(xmas_bottom_left(grid, x, y))
        )
    

print(s)
