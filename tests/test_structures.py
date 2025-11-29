# ruff: noqa
import pytest
from src.structures.stack_list import Stack
from src.structures.queue_list import Queue

class TestStack:
    """Тесты для стэка"""

    @pytest.mark.parametrize("max_size", [0, -1, -5])
    def test_invalid_stack_size(self, max_size):
        """Тест создания стэка с невалидным размером"""
        with pytest.raises(ValueError):
            Stack(max_size)

    def test_pop_empty_stack(self):
        """Тест извлечения из пустого стэка"""
        stack = Stack(5)
        with pytest.raises(IndexError, match="Error: Stack is empty"):
            stack.pop()

    def test_peek_empty_stack(self):
        """Тест просмотра вершины пустого стэка"""
        stack = Stack(5)
        with pytest.raises(IndexError, match="Error: Stack is empty"):
            stack.peek()

    def test_min_empty_stack(self):
        """Тест поиска минимума в пустом стэке"""
        stack = Stack(5)
        with pytest.raises(IndexError, match="Error: Stack is empty"):
            stack.min()

    def test_push_full_stack(self):
        """Тест добавления в переполненный стэк"""
        stack = Stack(2)
        stack.push(1)
        stack.push(2)
        with pytest.raises(IndexError, match="Error: Stack overflow"):
            stack.push(3)

    @pytest.mark.parametrize("elements,expected", [
        ([1, 2, 3], 3),
        ([5], 5),
        ([10, 20], 20),
    ])
    def test_peek(self, elements, expected):
        """Тест просмотра вершины стэка"""
        stack = Stack(len(elements) + 2)
        for el in elements:
            stack.push(el)
        assert stack.peek() == expected
        # Проверяем, что элемент не удалился
        assert stack.peek() == expected

    @pytest.mark.parametrize("elements,expected", [
        ([1, 2, 3], 3),
        ([5], 5),
        ([10, 20, 30, 40], 40),
    ])
    def test_pop(self, elements, expected):
        """Тест извлечения из стэка"""
        stack = Stack(len(elements) + 2)
        for el in elements:
            stack.push(el)
        assert stack.pop() == expected
        assert len(stack) == len(elements) - 1

    @pytest.mark.parametrize("elements,expected", [
        ([3, 1, 2], 1),
        ([5], 5),
        ([10, 5, 15, 3], 3),
        ([7, 7, 7], 7),
    ])
    def test_min(self, elements, expected):
        """Тест поиска минимума в стэке"""
        stack = Stack(len(elements) + 2)
        for el in elements:
            stack.push(el)
        assert stack.min() == expected

    @pytest.mark.parametrize("elements,expected", [
        ([], 0),
        ([1], 1),
        ([1, 2, 3], 3),
        ([5, 10, 15, 20], 4),
    ])
    def test_len(self, elements, expected):
        """Тест длины стэка"""
        stack = Stack(len(elements) + 5)
        for el in elements:
            stack.push(el)
        assert len(stack) == expected

    def test_is_empty(self):
        """Тест проверки пустоты стэка"""
        stack = Stack(5)
        assert stack.is_empty()
        stack.push(1)
        assert stack.is_empty()
        stack.pop()
        assert stack.is_empty()

    def test_is_full(self):
        """Тест проверки заполненности стэка"""
        stack = Stack(2)
        assert stack.is_full()
        stack.push(1)
        assert stack.is_full()
        stack.push(2)
        assert stack.is_full()


class TestQueue:
    """Тесты для очереди"""

    @pytest.mark.parametrize("max_size", [0, -1, -5])
    def test_invalid_queue_size(self, max_size):
        """Тест создания очереди с невалидным размером"""
        with pytest.raises(ValueError):
            Queue(max_size)

    def test_dequeue_empty_queue(self):
        """Тест извлечения из пустой очереди"""
        queue = Queue(5)
        with pytest.raises(IndexError, match="Error: Queue is empty"):
            queue.dequeue()

    def test_front_empty_queue(self):
        """Тест просмотра начала пустой очереди"""
        queue = Queue(5)
        with pytest.raises(IndexError, match="Error: Queue is empty"):
            queue.front()

    def test_enqueue_full_queue(self):
        """Тест добавления в переполненную очередь"""
        queue = Queue(2)
        queue.enqueue(1)
        queue.enqueue(2)
        with pytest.raises(IndexError, match="Error: Queue is full"):
            queue.enqueue(3)

    @pytest.mark.parametrize("elements,expected", [
        ([1, 2, 3], 1),
        ([5], 5),
        ([10, 20], 10),
    ])
    def test_front(self, elements, expected):
        """Тест просмотра начала очереди"""
        queue = Queue(len(elements) + 2)
        for el in elements:
            queue.enqueue(el)
        assert queue.front() == expected
        # Проверяем, что элемент не удалился
        assert queue.front() == expected

    @pytest.mark.parametrize("elements,expected", [
        ([1, 2, 3], 1),
        ([5], 5),
        ([10, 20, 30, 40], 10),
    ])
    def test_dequeue(self, elements, expected):
        """Тест извлечения из очереди"""
        queue = Queue(len(elements) + 2)
        for el in elements:
            queue.enqueue(el)
        assert queue.dequeue() == expected
        assert len(queue) == len(elements) - 1

    @pytest.mark.parametrize("elements,expected", [
        ([], 0),
        ([1], 1),
        ([1, 2, 3], 3),
        ([5, 10, 15, 20], 4),
    ])
    def test_len_queue(self, elements, expected):
        """Тест длины очереди"""
        queue = Queue(len(elements) + 5)
        for el in elements:
            queue.enqueue(el)
        assert len(queue) == expected

    def test_is_empty_queue(self):
        """Тест проверки пустоты очереди"""
        queue = Queue(5)
        assert queue.is_empty()
        queue.enqueue(1)
        assert queue.is_empty()
        queue.dequeue()
        assert queue.is_empty()

    def test_is_full_queue(self):
        """Тест проверки заполненности очереди"""
        queue = Queue(2)
        assert queue.is_full()
        queue.enqueue(1)
        assert queue.is_full()
        queue.enqueue(2)
        assert queue.is_full()

    def test_circular_behavior(self):
        """Тест кольцевого поведения очереди"""
        queue = Queue(3)
        # Заполняем очередь
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # Извлекаем два элемента
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2

        # Добавляем новые элементы - должны использовать освободившееся место
        queue.enqueue(4)
        queue.enqueue(5)

        # Проверяем порядок извлечения
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5
        assert queue.is_empty()

    @pytest.mark.parametrize("operations,expected_length", [
        (['enqueue', 'enqueue', 'dequeue', 'enqueue'], 2),
        (['enqueue', 'dequeue', 'enqueue', 'enqueue'], 2),
        (['enqueue', 'enqueue', 'enqueue', 'dequeue', 'dequeue'], 1),
    ])
    def test_mixed_operations(self, operations, expected_length):
        """Тест смешанных операций с очередью"""
        queue = Queue(5)
        value = 1
        for op in operations:
            if op == 'enqueue':
                queue.enqueue(value)
                value += 1
            elif op == 'dequeue':
                if not queue.is_empty():
                    queue.dequeue()

        assert len(queue) == expected_length


# Дополнительные тесты для проверки корректности данных
class TestDataIntegrity:
    """Тесты целостности данных"""

    def test_stack_data_integrity(self):
        """Тест целостности данных в стэке"""
        stack = Stack(5)
        test_data = [10, 20, 30, 40, 50]

        for data in test_data:
            stack.push(data)

        # Проверяем, что данные сохранились в правильном порядке
        assert stack.body[:len(stack)] == test_data

        # Проверяем извлечение в обратном порядке
        for i in range(len(test_data)-1, -1, -1):
            assert stack.pop() == test_data[i]

    def test_queue_data_integrity(self):
        """Тест целостности данных в очереди"""
        queue = Queue(5)
        test_data = [10, 20, 30, 40, 50]

        for data in test_data:
            queue.enqueue(data)

        # Проверяем извлечение в правильном порядке (FIFO)
        for data in test_data:
            assert queue.dequeue() == data

        assert queue.is_empty()
