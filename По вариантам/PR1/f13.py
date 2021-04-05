import math


def f13(n):
    p1 = p2 = 0
    for i in range(1, n + 1):
        p1 += math.tan(math.log(i) - ((i ** 3) / 67) - 31) + i ** 2
    for i in range(1, n + 1):
        p2 += 75 * i ** 4 + i
    return p1 - p2
