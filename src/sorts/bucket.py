def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
    Карманная сортировка для вещественных чисел
    """
    str_exists = [1 for x in a if isinstance(x, str)]
    if str_exists:
        print("Bucket sort не сортирует строки.")
        raise TypeError

    buckets_count = buckets if buckets is not None else len(a)
    buckets_array: list[list[float]] = [[] for _ in range(buckets_count)]

    min_el, max_el = min(a), max(a)
    for el in a:
        normalized = (el - min_el) / (max_el - min_el + 1e-12)
        # 1e-12 во избежание деления на ноль

        index = int(normalized * buckets_count)

        # если normalized = 1.0, т.е. если el = max_el
        if index == buckets_count:
            index = buckets_count - 1

        buckets_array[index].append(el)
    for i in range(buckets_count):
        if len(buckets_array[i]) == 0:
            continue
        buckets_array[i] = insertion_sort(buckets_array[i])

    # Объединение корзин
    result = []
    for bucket in buckets_array:
        result.extend(bucket)

    return result


def insertion_sort(a: list[float]):
    """
    Сортировка вставками для вещественных чисел
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1   # берём индекс предыдущего элемента
        while j >= 0 and a[j] > key:    # в цикле по сути перемещаем key (текущий элемент) вниз (уменьшаем индекс),
                                        # пока key не станет больше или равен предыдущего элемента, то есть не встанет на своё место
                                        # всё до индекса i - 1 гарантированно уже сортированно
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

    return a
