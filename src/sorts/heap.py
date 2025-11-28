# # Куча минимума  - вершина <= потомки   Корень - минимум
# # Куча максимума - вершина >= потомки   Корень - максимум

# # Priority queue - очередь с приоритетами (другое название)
# class Heap:
#     def __init__(self, array: list[int]):
#         self.array = array
#         self.heap_size = len(array)

#     def swap(self, vertex1: int, vertex2: int) -> None:
#         self.array[vertex1], self.array[vertex2] = self.array[vertex2], self.array[vertex1]

#     def sift_up(self, vertex: int) -> None:
#         # Вершина >
#         while vertex > 1 and self.array[vertex] < self.array[vertex / 2]:
#             self.swap(vertex, vertex / 2)
#             vertex /= 2
