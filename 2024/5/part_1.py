with open('input.txt', 'r') as f:
    data = f.read()

order, updates = data.split('\n\n')
order = order.split('\n')
updates = updates.split('\n')

orders = {}
s = 0
for x in order:
    a, b = map(int, x.split('|'))
    orders[(a, b)] = True
    orders[(b, a)] = False

for update in updates[:-1]:
    update = list(map(int, update.split(',')))
    invalid = False
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if (update[i], update[j]) in orders and orders[(update[i], update[j])] is False:
                invalid = True
                break

    if not invalid:
        s += (update[len(update) // 2])

print(s)
