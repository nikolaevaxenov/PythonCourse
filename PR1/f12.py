import math


def f12(x):
    if x < 93:
        return 30 * (((x ** 7) / 67) + 46 * x ** 4 - 12) ** 4 - math.cos(x)
    elif 93 <= x < 166:
        return (((x ** 7) / 65) - 56 * x ** 3) ** 2
    elif 166 <= x < 239:
        return x ** 3 + math.exp(x)
    elif 239 <= x < 258:
        return math.sin(42 * x ** 6 - x - 21) - math.sin(x) + 47
    else:
        return ((x ** 7) / 83) - 99 * x ** 5
