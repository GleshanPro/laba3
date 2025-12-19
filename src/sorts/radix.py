def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Цифровая сортировка, степень от 2 до 10 включительно
    """
    str_exists = [1 for x in a if isinstance(x, str)]
    if str_exists:
        print("- Radix Sort не сортирует строки.")
        raise TypeError

    minEl = min(a)
    if minEl < 0:
        print("- Нельзя использовать сортировку Radix с отрицательными числами, т.к. она использует сортировку подсчётом")
        raise ValueError
    if not all(isinstance(x, int) for x in a):
        print(" - Нельзя использовать сортировку Radix с типом float, т.к. она использует сортировку подсчётом")
        raise TypeError

    mx = max(a)
    result = a.copy()

    exp = 1
    while mx / exp >= 1:
        result = count_sort_radix(result, exp, base)
        exp *= base

    return result

def count_sort_radix(a: list[int], exp: int, base: int) -> list[int]:
    """
    Сортировка подсчётом для Radix Sort
    """
    n = len(a)

    # Frequency count
    counter = [0] * base    # Кол-во цифр
    for el in a:
        index = (el // exp) % base
        counter[index] += 1

    for i in range(1, base):
        counter[i] += counter[i - 1]

    result = [0] * n

    i = n - 1
    while i >= 0:
        index = (a[i] // exp) % base
        result[counter[index] - 1] = a[i]
        counter[index] -= 1
        i -= 1

    return result
