with open("input.txt", "r") as f:
    data = list(map(int, f.read().strip().split(" ")))


counts = {}
for i, x in enumerate(data):
    counts[x] = counts.get(x, 0) + 1


blinks = 75
for blink in range(blinks):
    new_counts = {}

    for stone in counts:
        str_stone = str(stone)
        if stone == 0:
            new_counts[1] = new_counts.get(1, 0) + counts[0]
        elif len(str_stone) % 2 == 0:
            left, right = (
                str_stone[: len(str_stone) // 2],
                str_stone[len(str_stone) // 2 :],
            )

            while len(right) > 1 and right[0] == "0":
                right = right[1:]

            new_counts[int(left)] = new_counts.get(int(left), 0) + counts[stone]
            new_counts[int(right)] = new_counts.get(int(right), 0) + counts[stone]
        else:
            new_counts[stone * 2024] = new_counts.get(stone * 2024, 0) + counts[stone]

    counts = new_counts

total_stones = sum(counts.values())
print(total_stones)
