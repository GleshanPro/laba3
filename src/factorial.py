def factorial(n: int) -> int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_resursive(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * factorial_resursive(n-1)
