import math


def f(y, x):
    sum = 0
    n = len(x) - 1
    for i in range(1, n + 2):
        sum += (y[n + 1 - i] ** 3 + 25 + x[n + 1 - math.ceil(i / 2)] ** 2) ** 4 / 73
    return sum


print(f([-0.29, -0.88, 0.08],
        [-0.26, 0.7, -0.07]))
print(f([-0.49, 0.41, -0.05],
        [-0.5, -0.84, 0.1]))
