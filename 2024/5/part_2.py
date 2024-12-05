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

def check_update(orders, update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if (update[i], update[j]) in orders and orders[(update[i], update[j])] is False:
                return False
    return True

invalids = []
for update in updates[:-1]:
    update = list(map(int, update.split(',')))
    if not check_update(orders, update):
        invalids.append(update)

for invalid in invalids:
    while not check_update(orders, invalid):
        for i in range(len(invalid)):
            for j in range(i + 1, len(invalid)):
                if (invalid[i], invalid[j]) in orders and orders[(invalid[i], invalid[j])] is False:
                    invalid[i], invalid[j] = invalid[j], invalid[i]

    s += (invalid[len(invalid) // 2])

print(s)
