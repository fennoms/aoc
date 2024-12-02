with open('input.txt', 'r') as f:
    data = f.read().splitlines()

valid = 0
for line in data:
    line = line.split()
    index_1, index_2 = map(int, line[0].split('-'))
    index_1 -= 1
    index_2 -= 1

    letter = line[1][0]
    password = line[2]

    if (password[index_1] == letter or password[index_2] == letter) and password[index_1] != password[index_2]:
        valid += 1
    
print(valid)
