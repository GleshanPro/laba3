# from src.sorts.counting import count_sort
# def radix_sort(a: list[int], base: int = 10) -> list[int]:
#     mx = max(a)

#     current_nums = a.copy()
#     digits = [0] * len(a)
#     for i in range(len(str(mx))):
#         for j, num in enumerate(current_nums):
#             digit = num % base
#             digits[j] = digit
#             current_nums[j] //= base
#         digits = count_sort(digits)
