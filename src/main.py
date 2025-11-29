# from src.factorial import factorial
# from src.factorial import factorial_resursive

# from src.fibonacci import fibo
# from src.fibonacci import fibo_resursive

# from src.sorts.radix import radix_sort
from src.sorts.bubble import bubble_sort
from src.sorts.bucket import bucket_sort
from src.sorts.count import count_sort
from src.sorts.heap import Heap
from src.sorts.quick import quick_sort
from src.sorts.radix import radix_sort

def array_input() -> list[float]:
    correct_input = False
    while not correct_input:
        try:
            array = [float(x) for x in input("Введите числа массива через пробел: ").split()]
            for i in range(len(array)):
                if int(array[i]) == array[i]:
                    array[i] = int(array[i])
            return array
        except:
            print("Некорректный ввод.")
 

def main() -> None:
    """
    Точка входа в приложение
    :return: Данная функция ничего не возвращает
    """
    goal = input("Здравствуйте! Зачем зашли?\n1) Сортировать массив\n2) Потыкать структуры данных\n3) Проверить факториал и фибоначи\n")
    match(goal):
        case "1":
            user_input = ""
            array = array_input()
            prev_array = []
            while user_input != 'q':
                print("\nВаш массив: ", *array)
                user_input = input("Выберите сортировку: \n1) Bubble\n2) Bucket\n3) Count\n4) Heap\n5) Quick\n6) Radix\n7) Обновить массив\n   'q' - выйти\n")
                
                new_array = []
                match(user_input):
                    case "1":
                        new_array = bubble_sort(array.copy())
                    case "2":
                        new_array = bucket_sort(array.copy())
                    case "3":
                        new_array = count_sort(array.copy())
                    case "4":
                        new_array = Heap.heap_sort(array.copy())
                    case "5":
                        new_array = quick_sort(array.copy())
                    case "6":
                        base = int(input("Основание системы счисления: "))
                        new_array = radix_sort(array.copy(), base)
                    case "7":
                        array = array_input()
                        continue
                    case "q":
                        break
                
                if new_array:
                    print("Ваш сортированный массив: ", *new_array)
                    if prev_array:
                        if prev_array == new_array:
                            print("Сортированный массив совпадает с предыдущим сортированным ✅")
                        else:   # Если всё правильно - не должно попадать сюда
                            print("Ошибка: cортированный массив НЕ совпадает с предыдущим сортированным ❌")
                    prev_array = new_array.copy()
                input("Продолжить >")
                    
                
    


if __name__ == "__main__":
    main()
