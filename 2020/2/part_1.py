with open('input.txt', 'r') as f:
    data = f.read().splitlines()

valid = 0
for line in data:
    line = line.split()
    min_count, max_count = map(int, line[0].split('-'))
    letter = line[1][0]
    password = line[2]

    if min_count <= password.count(letter) <= max_count:
        valid += 1
    
print(valid)
