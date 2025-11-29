def count_sort(a: list[int]) -> list[int]:
    """
    Сортировка подсчётом
    Эффективна для массивов с повторением чисел, желательно длина массива сопоставима максимальному числу в нём
    """
    if not all(isinstance(x, int) for x in a):
        print(" - Нельзя использовать сортировку подсчётом с типом float")
        return []
        
    minEl = min(a)
    if minEl < 0:
        print("- Нельзя использовать сортировку подсчётом с отрицательными числами")
        return []
    
    n = len(a)
    maxEl = max(a)

    # Frequency count
    counter = [0] * (maxEl+1)
    for el in a:
        counter[el] += 1
    result = [0] * n

    i = 0
    for num, count in enumerate(counter):
        border = i + count
        while i < border:
            result[i] = num
            i += 1
    return result
