from src.sorts.heap import Heap
class Stack:
    def __init__(self, max_size):
        if max_size <= 0:
            raise ValueError("Stack size must be positive")
        self.body = [0] * max_size
        self.i_ptr = -1
        self.max_size = max_size

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Error: Stack is empty\n")

        popped_el = self.body[self.i_ptr]
        self.i_ptr -= 1
        return popped_el

    def push(self, x: int) -> None:
        if self.is_full():
            raise IndexError("Error: Stack overflow\n")

        self.i_ptr += 1
        self.body[self.i_ptr] = x

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Error: Stack is empty\n")

        return self.body[self.i_ptr]

    def is_empty(self) -> bool:
        return self.i_ptr == -1

    def is_full(self) -> bool:
        return self.i_ptr + 1 >= self.max_size

    # O(n)
    def min(self) -> int:
        if self.is_empty():
            raise IndexError("Error: Stack is empty")

        # Брать только заполненную часть стэка
        stack_elements = self.body[:self.i_ptr + 1]
        heap = Heap.build_heap(stack_elements)
        return heap.min()

    def __len__(self) -> int:
        return self.i_ptr + 1
