# Thanks to hyperneutrino https://www.youtube.com/watch?v=layyhtQQuM0&t=446s
# for the explanation using a BFS instead of a DFS.

from collections import deque


with open("input.txt", "r") as f:
    grid = [list(map(int, row)) for row in f.read().splitlines()]

trailheads = {
    (x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 0
}


def in_grid(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


s = 0
for tx, ty in trailheads:
    Q = deque([(tx, ty)])
    seen = set((tx, ty))

    while len(Q) > 0:
        x, y = Q.popleft()

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for r, c in directions:
            nx, ny = x + r, y + c
            if not in_grid(nx, ny):
                continue

            if grid[nx][ny] != grid[x][y] + 1:
                continue

            if (nx, ny) in seen:
                continue
            seen.add((nx, ny))

            if grid[nx][ny] == 9:
                s += 1
            else:
                Q.append((nx, ny))

print(s)
