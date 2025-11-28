# O(n ^ 2)
def bubble_sort(a: list[int]) -> list[int]:
    """
    Сортировка пузырьком
    """
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(1, n-i):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swapped = True
        if not swapped:
            break

    return a
