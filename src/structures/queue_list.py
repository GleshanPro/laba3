class Queue:
    def __init__(self, max_size):
        if max_size <= 0:
            raise ValueError("Queue size must be positive")
        self.body = [0] * max_size
        self.head = 0
        self.tail = 0
        self.count = 0
        self.max_size = max_size

    def enqueue(self, x: int) -> None:
        if self.is_full():
            raise IndexError("Error: Queue is full")

        self.body[self.tail] = x
        self.tail = (self.tail + 1) % self.max_size
        self.count += 1

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("Error: Queue is empty")

        dequeued_el = self.body[self.head]
        self.head = (self.head + 1) % self.max_size
        self.count -= 1
        return dequeued_el

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count >= self.max_size

    def front(self) -> int:
        if self.is_empty():
            raise IndexError("Error: Queue is empty")

        return self.body[self.head]

    def __len__(self) -> int:
        return self.count
