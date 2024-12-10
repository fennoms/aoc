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

def find_empty_block(length):

    for l in range(len(blocks)):
        r = l + length - 1

        if r >= len(blocks):
            return None
    
        if all([blocks[i] == '.' for i in range(l, r + 1)]):
            return l
        
    return None
        

l = len(blocks) - 1
r = len(blocks) - 1

while l > 0:
    while blocks[r] == '.':
        r -= 1
    
    l = r
    while blocks[l - 1] == blocks[r]:
        l -= 1
    
    length = r - l + 1

    empty_idx = find_empty_block(length)

    if empty_idx is None:
        l -= length
        r -= length
        continue

    if empty_idx < l:
        for i in range(length):
            blocks[empty_idx + i] = blocks[l + i]
            blocks[l + i] = '.'

    l -= length
    r -= length

print(sum([i * x for i, x in enumerate(blocks) if x != '.']))
