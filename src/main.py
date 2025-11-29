# from src.factorial import factorial
# from src.factorial import factorial_resursive

# from src.fibonacci import fibo
# from src.fibonacci import fibo_resursive

from src.sorts.bubble import bubble_sort
from src.sorts.bucket import bucket_sort
from src.sorts.count import count_sort
from src.sorts.heap import Heap
from src.sorts.quick import quick_sort
from src.sorts.radix import radix_sort

from src.structures.stack import Stack

def array_input() -> list[float]:
    correct_input = False
    while not correct_input:
        try:
            array = input("Введите элементы массива через пробел: ").split()
            for i in range(len(array)):
                try:
                    array[i] = float(array[i])
                    if array[i] == int(array[i]):
                        array[i] = int(array[i])
                except:
                    pass
                        
            return array
        except:
            print("Некорректный ввод.")
            

def num_input(text: str) -> int:
    correct_input = False
    while not correct_input:
        try:
            num = int(input(text))
            return num
        except:
            print("Введите число.")
    
 

def main() -> None:
    """
    Точка входа в приложение
    :return: Данная функция ничего не возвращает
    """
    user_input = ""
    while True:
        goal = input("Здравствуйте! Зачем зашли? (в любой части программы напишите 'q', чтобы вернуться назад или выйти) \n1) Сортировать массив\n2) Потыкать структуры данных\n3) Проверить факториал и фибоначи\n")
        user_input = goal
        match(goal):
            case "1":
                array = array_input()
                prev_array = []
                while user_input != 'q':
                    print("\nВаш массив: ", *array)
                    user_input = input("Выберите сортировку: \n1) Bubble\n2) Bucket\n3) Count\n4) Heap\n5) Quick\n6) Radix\n7) Обновить массив\n")
                    
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
                            prev_array = []
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
            case "2":
                while True:
                    user_input = input("Выберите структуру данных:\n1) Стэк\n2) Очередь\n")
                    match(user_input):
                        case "1":
                            max_size = num_input("Введите максимальный размер стэка: ")
                            stack = Stack(max_size)
                            print("Вы создали cтэк. ")
                            while user_input != 'q':
                                user_input = input("\nВыберите действие:\n1) pop\n2) push\n3) min\n4) peek\n5) len\n6) Посмотреть стэк\n")
                                match(user_input):
                                    case "1":
                                        print(stack.pop())
                                    case "2":
                                        x = num_input("Введите число: ")
                                        stack.push(x)
                                    case "3":
                                        print(stack.min())
                                    case "4":
                                        print(stack.peek())
                                    case "5":
                                        print(len(stack)) # ?
                                    case "6":
                                        print(stack.body[:len(stack)])
                                    case "q":
                                        break
                                    
                        # case "2":
                        case "q":
                            break
            case "q":
                break
                    
                
    


if __name__ == "__main__":
    main()
