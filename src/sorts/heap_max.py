# Куча минимума  - вершина <= потомки   Корень - минимум
# Куча максимума - вершина >= потомки   Корень - максимум

# Слои кучи заполняются сверху вниз и слева направо, без "дырок"

# У нас - куча максимума.
# h = log(n) - высота дерева
# Priority queue - очередь с приоритетами (другое название)
# Индекс корня - 0
class HeapMax:
    def __init__(self, array: list[int]):
        self.array = array
        self.n = len(array)     # количество элементов в куче.

    def swap(self, vertex_index1: int, vertex_index2: int) -> None:
        self.array[vertex_index1], self.array[vertex_index2] = self.array[vertex_index2], self.array[vertex_index1]

    
    # Используется, когда значение элемента УМЕНЬШАЕТСЯ - он может стать больше родителя
    # O(h)
    def sift_up(self, vertex: int) -> None:
        # Вершина <= родителя - всё нормально.
        while vertex > 0 and self.array[vertex] > self.array[HeapMax.parent_vertex(vertex)]:
            # Вершина > родителя - поменять местами
            self.swap(vertex, HeapMax.parent_vertex(vertex))
            vertex = HeapMax.parent_vertex(vertex)
            
    # Используется, когда значение элемента УВЕЛИЧИВАЕТСЯ - он может стать меньше одного или двух потомков
    # O(h)        
    def sift_down(self, vertex: int) -> None:
        while (vertex * 2 + 1 < self.n):
            l = vertex * 2 + 1     # левый сын
            r = vertex * 2 + 2  # правый сын
            
            # Вернуть сей код потом
            son = -1
            if r < self.n and self.array[r] > self.array[l]:
                son = r
            elif l < self.n:
                son = l
            
            if self.array[vertex] >= self.array[son]:   # инвариант и так выполняется
                break
            
            self.swap(vertex, son)
            vertex = son
          
    # O(1)
    def max(self):
        return self.array[0]       
    # O(n)
    @staticmethod   # Статический метод - вызывается в самом классе, а не в его экземплярах.
    def build_heap(array: list[int]):
        heap = HeapMax(array.copy())
        """
        У Самира deepcopy, но copy достаточно, т.к. на вход не может подаваться список со вложенными списками
        """  
        
        # Листья - элементы кучи с индексами от n//2 до n-1 
        # У них нет потомков, поэтому нет смысла вызывать sift_down для них
        for i in range(len(array) // 2 - 1, -1, -1):
            heap.sift_down(i)
        return heap
    
    # O(n log n)
    @staticmethod
    def heap_sort(a: list[int]):
        """
        Сортировка кучей
        """
        n = len(a)
        if n <= 1:
            return a
        
        # Создаём кучу (максимальный элемент всегда с индексом 0)
        heap = HeapMax.build_heap(a.copy())
        
        # Ставим максимумы в конец
        for _ in range(n):
            heap.swap(0, heap.n - 1)
            heap.n -= 1    # Уменьшаем индекс конца
            
            # Ставим следующий минимум в начало
            if heap.n > 0:
                heap.sift_down(0)
                
        # Теперь не нужно делать reverse, как в куче минимума        
        return heap.array
        
    
    @staticmethod
    def parent_vertex(vertex_index: int):
        return (vertex_index-1) // 2
            