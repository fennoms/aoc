with open('input.txt', 'r') as f:
    data = f.read().strip().splitlines()

def correct_equation(target, numbers):
    if len(numbers) == 0:
        return target == 0

    if target % numbers[-1] == 0:
        if correct_equation(target // numbers[-1], numbers[:-1]):
            return True
    if correct_equation(target - numbers[-1], numbers[:-1]):
        return True

    return False


s = 0
for equation in data:
    target, numbers = equation.split(': ')
    target = int(target)
    numbers = list(map(int, numbers.split()))

    if correct_equation(target, numbers):
        s += target

print(s)
