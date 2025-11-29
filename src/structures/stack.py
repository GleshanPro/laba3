from src.sorts.heap import Heap
class Stack:
    def __init__(self, max_size):
        self.body = [0] * max_size
        self.i_ptr = -1
        self.max_size = max_size
    
    def pop(self) -> int:
        if self.is_empty():
            print("Error: Stack is empty\n")
            return
        
        popped_el = self.body[self.i_ptr]
        self.i_ptr -= 1
        return popped_el

    def push(self, x: int) -> None:
        if self.is_full():
            print("Error: Stack overflow\n")
            return
        
        self.i_ptr += 1
        self.body[self.i_ptr] = x
        

    def is_empty(self) -> bool:
        return self.i_ptr == -1
    
    def is_full(self) -> bool:
        return self.i_ptr + 1 >= self.max_size

    # O(n)
    def min(self) -> int:
        heap = Heap.build_heap(self.body)
        return heap.min()
        

    def peek(self) -> int:
        return self.body[self.i_ptr]

    def __len__(self) -> int:
        return self.i_ptr + 1
