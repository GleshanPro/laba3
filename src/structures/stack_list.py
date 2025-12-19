class Stack:
    def __init__(self, max_size: int):
        if max_size <= 0:
            raise ValueError("Stack size must be positive")
        self.body = []
        self.min_els = []   # массив минимумов
        self.max_size = max_size
        

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Error: Stack is empty\n")
        
        self.min_els.pop()
        
        return self.body.pop()

    def push(self, x: int) -> None:
        if self.is_full():
            raise IndexError("Error: Stack overflow\n")

        
        if not self.is_empty():
            current_min = min(x, self.min_els[-1])
        else:
            current_min = x
        self.min_els.append(current_min)

        self.body.append(x)

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Error: Stack is empty\n")

        return self.body[-1]

    def is_empty(self) -> bool:
        return len(self.body) == 0

    def is_full(self) -> bool:
        return len(self.body) >= self.max_size

    # O(1)
    def min(self) -> int:
        if self.is_empty():
            raise IndexError("Error: Stack is empty")

        return self.min_els[-1]

    def __len__(self) -> int:
        return len(self.body)