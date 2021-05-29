import math


def f14(n):
    if n == 0:
        return 3
    else:
        return f14(n - 1) / 6 + math.sin(f14(n - 1))
