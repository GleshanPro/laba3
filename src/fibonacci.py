from functools import lru_cache
# O(n)
def fibo(n: int) -> int:
    if n < 1:
        raise ValueError("Числа Фибоначчи начинают индексироваться с 1")

    if n == 1:
        return 0

    prev1 = 0
    prev2 = 1
    result = 1
    for _ in range(1, n - 1):
        result = prev1 + prev2

        prev1 = prev2
        prev2 = result
    return result

@lru_cache(None)
def fibo_resursive(n: int) -> int:
    """
    Returns fibonacci element of index n (! - 1st element is 1st element and = 0, 0th element doesn't exist)

    :param n: Index of element. n >= 1
    :type n: int
    :return: Fibonacci element of index n
    :rtype: int
    """
    if n < 1:
        raise ValueError("Числа Фибоначчи начинают индексироваться с 1")

    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo_resursive(n-1) + fibo_resursive(n-2)
