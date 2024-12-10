with open('input.txt', 'r') as f:
    diskmap = list(map(int, list(f.read().strip())))

blocks = []

id = 0
for i, x in enumerate(diskmap):
    if i % 2 == 0:
        blocks += [id] * x
        id += 1
    else:
        blocks += ['.'] * x


l = 0
r = len(blocks) - 1

while l < r:

    while blocks[l] != '.':
        l += 1

    while blocks[r] == '.':
        r -= 1

    blocks[l], blocks[r] = blocks[r], blocks[l]
    l += 1
    r -= 1

print(sum([i * x for i, x in enumerate(blocks) if x != '.']))
