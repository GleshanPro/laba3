from functools import lru_cache
# O(n)
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Нельзя брать факториал отрицательного числа")

    result = 1
    for i in range(1, n+1):
        result *= i
    return result

@lru_cache(None)
def factorial_resursive(n: int) -> int:
    if n < 0:
        raise ValueError("Нельзя брать факториал отрицательного числа")

    if n in (0, 1):
        return 1
    return
