def count_sort(a: list[int]) -> list[int]:
    """
    Сортировка подсчётом
    Эффективна для массивов с повторением чисел, желательно длина массива сопоставима максимальному числу в нём
    """
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

print(count_sort([0,9,1,2,3,5,3,1,23,4,6,1,3,5,6,7]))
