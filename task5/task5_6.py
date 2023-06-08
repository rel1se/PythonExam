import math


def f(x, z):
    sum = 0
    n = len(x) - 1
    for i in range(1, n + 2):
        sum += 53 * x[n + 1 - math.ceil(i / 4)] ** 2 + 86 * x[n + 1 - i] ** 3 + 94 * z[n + 1 - i]
    return 75 * sum


print(f([0.78, 0.54, 0.72, -0.23, -0.47],
        [0.59, -0.97, -0.53, 0.57, 0.19]))
