import math


def f(x):
    sum = 0
    n = len(x) - 1
    for i in range(1, n + 2):
        sum += 32 * (51 * x[n + 1 - math.ceil(i / 3)] - 95 - x[n + 1 - i] ** 3 / 53)
    return sum


print(f([-0.47, 0.52, 0.45, 0.09, 0.75, -0.34, -0.03, -0.22]))
print(f([0.73, 0.61, -0.3, -0.6, 0.2, -0.73, -0.23, 0.8]))
