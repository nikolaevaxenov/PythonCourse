import re


def p5(hypertext: str) -> str:
    """
    Транслятор, который удаляет HTML-теги и оставляет обычный текст
    """
    return re.sub('<[^>]*>', '', hypertext)


def sqrt_func(x: float, epsilon: float) -> float:
    """
    Square Root
    Newton-Raphson method implementation.
    """
    approx = x / 2
    while abs(x - approx) > epsilon:
        approx = 0.5 * (approx + x / approx)
    return approx