# O(n log n) - average
# O(n^2) - worst
def quick_sort(a: list[int]) -> list[int]:
    """
    Быстрая сортировка с помощью опорной точки (pivot) и рекурсивного разделения массива
    на элементы большие (l), равные (m) и меньшие pivot (l)
    """
    if len(a) <= 1:
        return a
    
    pivot = a[len(a) // 2]
    
    l = [x for x in a if x < pivot]
    m = [x for x in a if x == pivot] # middle
    r = [x for x in a if x > pivot]
    
    return quick_sort(l) + m + quick_sort(r)