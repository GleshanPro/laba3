# ruff: noqa
import pytest
import random
from src.sorts.bubble import bubble_sort
from src.sorts.bucket import bucket_sort
from src.sorts.count import count_sort
from src.sorts.heap_min import HeapMin
from src.sorts.heap_max import HeapMax
from src.sorts.quick import quick_sort
from src.sorts.radix import radix_sort

class TestSortingAlgorithms:
    """Тесты для алгоритмов сортировки"""

    # Общие тесты для всех сортировок
    @pytest.mark.parametrize("sort_func", [
        bubble_sort,
        HeapMax.heap_sort,
        quick_sort,
    ])
    def test_empty_array(self, sort_func):
        """Тест пустого массива"""
        assert sort_func([]) == []

    @pytest.mark.parametrize("sort_func", [
        bubble_sort,
        lambda x: bucket_sort(x, 5),
        count_sort,
        HeapMax.heap_sort,
        quick_sort,
        lambda x: radix_sort(x, 10)
    ])
    def test_single_element(self, sort_func):
        """Тест массива с одним элементом"""
        assert sort_func([5]) == [5]

    @pytest.mark.parametrize("sort_func", [
        bubble_sort,
        lambda x: bucket_sort(x, 5),
        count_sort,
        HeapMax.heap_sort,
        quick_sort,
        lambda x: radix_sort(x, 10)
    ])
    def test_already_sorted(self, sort_func):
        """Тест уже отсортированного массива"""
        assert sort_func([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    @pytest.mark.parametrize("sort_func", [
        bubble_sort,
        lambda x: bucket_sort(x, 5),
        count_sort,
        HeapMax.heap_sort,
        quick_sort,
        lambda x: radix_sort(x, 10)
    ])
    def test_reverse_sorted(self, sort_func):
        """Тест обратно отсортированного массива"""
        assert sort_func([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    @pytest.mark.parametrize("sort_func", [
        bubble_sort,
        lambda x: bucket_sort(x, 5),
        count_sort,
        HeapMax.heap_sort,
        quick_sort,
        lambda x: radix_sort(x, 10)
    ])
    def test_duplicates(self, sort_func):
        """Тест массива с дубликатами"""
        assert sort_func([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]

    @pytest.mark.parametrize("sort_func", [
        bubble_sort,
        lambda x: bucket_sort(x, 5),
        count_sort,
        HeapMax.heap_sort,
        quick_sort,
        lambda x: radix_sort(x, 10)
    ])
    def test_random_arrays(self, sort_func):
        """Тест случайных массивов"""
        for _ in range(10):  # 10 случайных тестов
            arr = [random.randint(1, 100) for _ in range(20)]
            expected = sorted(arr)
            assert sort_func(arr) == expected


class TestBubbleSort:
    """Тесты для пузырьковой сортировки"""

    def test_bubble_sort_specific_cases(self):
        """Специфичные тесты для bubble sort"""
        # Тест с отрицательными числами
        assert bubble_sort([3, -1, 2, -5, 4]) == [-5, -1, 2, 3, 4]

        # Тест с нулями
        assert bubble_sort([0, 5, 0, 2, 0]) == [0, 0, 0, 2, 5]

        # Тест с большими числами
        assert bubble_sort([1000, 1, 100, 10]) == [1, 10, 100, 1000]


class TestBucketSort:
    """Тесты для карманной сортировки"""

    @pytest.mark.parametrize("buckets", [1, 5, 10, 20])
    def test_different_bucket_sizes(self, buckets):
        """Тест с разным количеством карманов"""
        arr = [0.1, 0.5, 0.3, 0.8, 0.2]
        assert bucket_sort(arr, buckets) == [0.1, 0.2, 0.3, 0.5, 0.8]

    def test_float_numbers(self):
        """Тест с вещественными числами"""
        arr = [0.42, 0.32, 0.99, 0.01, 0.75]
        assert bucket_sort(arr, 5) == [0.01, 0.32, 0.42, 0.75, 0.99]

    def test_uniform_distribution(self):
        """Тест с равномерным распределением"""
        arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        assert bucket_sort(arr, 10) == arr

    def test_string_input(self):
        """Тест со строковым вводом"""
        with pytest.raises(TypeError):
            bucket_sort(["a", "b", "c"], 5)

    def test_edge_case_buckets(self):
        """Тест граничных случаев с карманами"""
        arr = [0.1, 0.5, 0.9]
        # 1 карман - вся сортировка делается insertion sort
        assert bucket_sort(arr, 1) == [0.1, 0.5, 0.9]
        # Карманов больше чем элементов
        assert bucket_sort(arr, 10) == [0.1, 0.5, 0.9]


class TestCountSort:
    """Тесты для сортировки подсчётом"""

    def test_positive_integers(self):
        """Тест с положительными целыми"""
        assert count_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

    def test_with_zeros(self):
        """Тест с нулями"""
        assert count_sort([0, 5, 0, 2, 0]) == [0, 0, 0, 2, 5]

    def test_single_number_repeated(self):
        """Тест с повторяющимся числом"""
        assert count_sort([3, 3, 3, 3]) == [3, 3, 3, 3]

    def test_negative_numbers(self):
        """Тест с отрицательными числами"""
        with pytest.raises(ValueError):
            count_sort([3, -1, 2])
            

    def test_float_numbers_count_sort(self):
        """Тест с вещественными числами"""
        with pytest.raises(TypeError):
            count_sort([3.5, 1.2, 2.7])

    def test_string_input_count_sort(self):
        """Тест с строковым вводом"""
        with pytest.raises(TypeError):
            count_sort(["a", "b", "c"])


class TestHeapMin:
    """Тесты для сортировки кучей максимума"""

    def test_heap_class_methods(self):
        """Тест методов класса Heap"""
        arr = [4, 2, 8, 1, 3]
        heap = HeapMax.build_heap(arr)

        # Проверяем, что максимум корректен
        assert heap.max() == 8

        # Проверяем, что исходный массив не изменился
        assert arr == [4, 2, 8, 1, 3]

    def test_heap_sort_comprehensive(self):
        """Комплексный тест heap sort"""
        # Тест с отрицательными числами
        assert HeapMax.heap_sort([3, -1, 2, -5, 4]) == [4, 3, 2, -1, -5]

        # Тест с большим диапазоном
        assert HeapMax.heap_sort([100, 1, 1000, 10]) == [1000, 100, 10, 1]

        # Тест с повторениями
        assert HeapMax.heap_sort([5, 3, 5, 1, 3]) == [5, 5, 3, 3, 1]

    def test_heap_invariants(self):
        """Тест инвариантов кучи"""
        arr = [random.randint(1, 100) for _ in range(20)]
        heap = HeapMax.build_heap(arr)

        # Проверяем инвариант кучи для всех элементов
        for i in range(len(heap.array)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap.array):
                assert heap.array[i] >= heap.array[left]
            if right < len(heap.array):
                assert heap.array[i] >= heap.array[right]
                
class TestHeapMin:
    """Тесты для кучи минимума"""

    def test_heap_class_methods(self):
        """Тест методов класса Heap"""
        arr = [4, 2, 8, 1, 3]
        heap = HeapMin.build_heap(arr)

        # Проверяем, что минимум корректен
        assert heap.min() == 1

        # Проверяем, что исходный массив не изменился
        assert arr == [4, 2, 8, 1, 3]


    def test_heap_invariants(self):
        """Тест инвариантов кучи"""
        arr = [random.randint(1, 100) for _ in range(20)]
        heap = HeapMin.build_heap(arr)

        # Проверяем инвариант кучи для всех элементов
        for i in range(len(heap.array)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap.array):
                assert heap.array[i] <= heap.array[left]
            if right < len(heap.array):
                assert heap.array[i] <= heap.array[right]


class TestQuickSort:
    """Тесты для быстрой сортировки"""

    def test_quick_sort_pivot_behavior(self):
        """Тест поведения с разными опорными элементами"""
        # Массив где средний элемент - хороший pivot
        assert quick_sort([3, 6, 1, 8, 2]) == [1, 2, 3, 6, 8]

        # Массив с одинаковыми элементами
        assert quick_sort([5, 5, 5, 5]) == [5, 5, 5, 5]

        # Массив где все элементы меньше pivot
        assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_quick_sort_edge_cases(self):
        """Граничные случаи для quick sort"""
        # Очень большой диапазон
        assert quick_sort([1000, 1, 100000, 10]) == [1, 10, 1000, 100000]

        # С отрицательными числами
        assert quick_sort([0, -5, 5, -10, 10]) == [-10, -5, 0, 5, 10]

        # Смешанные типы данных (только целые)
        assert quick_sort([1, 3, 2]) == [1, 2, 3]


class TestRadixSort:
    """Тесты для цифровой сортировки"""

    @pytest.mark.parametrize("base", [2, 8, 10, 16])
    def test_different_bases(self, base):
        """Тест с разными основаниями систем счисления"""
        arr = [170, 45, 75, 90, 2, 802, 24, 66]
        assert radix_sort(arr, base) == [2, 24, 45, 66, 75, 90, 170, 802]

    def test_same_length_numbers(self):
        """Тест с числами одинаковой длины"""
        assert radix_sort([123, 456, 789, 234, 567]) == [123, 234, 456, 567, 789]

    def test_different_length_numbers(self):
        """Тест с числами разной длины"""
        assert radix_sort([1, 23, 456, 7890, 12]) == [1, 12, 23, 456, 7890]

    def test_with_zeros_radix(self):
        """Тест с нулями"""
        assert radix_sort([0, 100, 0, 50, 0]) == [0, 0, 0, 50, 100]

    def test_negative_numbers_radix(self):
        """Тест с отрицательными числами"""
        with pytest.raises(ValueError):
            radix_sort([3, -1, 2])

    def test_float_numbers_radix(self):
        """Тест с вещественными числами"""
        with pytest.raises(TypeError):
            radix_sort([3.5, 1.2, 2.7])

    def test_string_input_radix(self):
        """Тест с строковым вводом"""
        with pytest.raises(TypeError):
            radix_sort(["a", "b", "c"])


class TestPerformance:
    """Тесты производительности (проверка корректности на больших данных)"""

    @pytest.mark.parametrize("sort_func", [
        bubble_sort,
        lambda x: bucket_sort(x, 100),
        count_sort,
        quick_sort,
        lambda x: radix_sort(x, 10)
    ])
    def test_large_array(self, sort_func):
        """Тест на большом массиве"""
        arr = [random.randint(1, 1000) for _ in range(100)]
        expected = sorted(arr)
        result = sort_func(arr)
        assert result == expected

    def test_sorted_large_array(self):
        """Тест на большом отсортированном массиве"""
        arr = list(range(100))
        expected = arr.copy()

        # Все сортировки должны сохранить порядок
        assert bubble_sort(arr.copy()) == expected
        assert bucket_sort(arr.copy(), 50) == expected
        assert count_sort(arr.copy()) == expected
        assert quick_sort(arr.copy()) == expected
        assert radix_sort(arr.copy(), 10) == expected


class TestErrorCases:
    """Тесты обработки ошибок"""

    def test_none_input(self):
        """Тест с None входом"""
        # Проверяем, что функции не падают с None
        for sort_func in [bubble_sort, count_sort, quick_sort]:
            with pytest.raises(Exception):
                sort_func(None)

    def test_invalid_types(self):
        """Тест с невалидными типами данных"""
        # Mix of types
        mixed_arr = [1, "a", 3]
        for sort_func in [bubble_sort, quick_sort]:
            with pytest.raises(Exception):
                sort_func(mixed_arr)
