# Реализовать функцию, оперирующую векторами длины n

import math


def main(x, z):
    sum = 0
    n = len(x)
    for i in range(0, n):
        sum += 86 * pow(math.log10(7 + pow(z[math.ceil(i // 4)], 2)
                                   + x[i]), 6)
    return 77 * sum


print(main([-0.96, -0.59, 0.89, 0.86, 0.38, 0.68, -0.81], [-0.97, 0.43, -0.79, -0.74, -0.76, 0.86, 0.71]))
