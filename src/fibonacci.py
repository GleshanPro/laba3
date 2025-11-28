def fibo(n: int) -> int:
    result = 0
    for i in range(1, n+1):
        result += i
    return result


def fibo_resursive(n: int) -> int:
    """
    Returns fibonacci element of index n (! - 1st element is 1st element and = 0, 0th element doesn't exist)
    
    :param n: Index of element. n >= 1
    :type n: int
    :return: Fibonacci element of index n
    :rtype: int
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo_resursive(n-1) + fibo_resursive(n-2)
