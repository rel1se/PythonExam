import math


def f(x, y, z):
    sum = 0
    n = len(x) - 1
    for i in range(1, n + 2):
        sum += (x[i - 1] ** 3 - z[math.ceil(i / 2 - 1)] ** 2 - y[math.ceil(i / 3 - 1)]) ** 7
    return sum


print(f([0.39, 0.44, 0.73, 0.21, -0.12, 0.22, 0.11, 0.39],
        [-0.42, 0.73, -0.3, -0.35, 0.54, 0.13, -0.82, -0.0],
        [0.67, 0.77, -0.65, 0.18, 0.5, 0.3, 0.76, -0.96]))
