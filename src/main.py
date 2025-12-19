from src.factorial import factorial
from src.factorial import factorial_resursive

from src.fibonacci import fibo
from src.fibonacci import fibo_resursive

from src.sorts.bubble import bubble_sort
from src.sorts.bucket import bucket_sort
from src.sorts.count import count_sort
from src.sorts.heap_max import HeapMax
from src.sorts.quick import quick_sort
from src.sorts.radix import radix_sort

from src.structures.stack_list import Stack
from src.structures.queue_list import Queue

from src.common.config import LOGGING_CONFIG
import logging

def array_input() -> list[float]:
    array = input("Введите элементы массива через пробел: ").split()
    try:
        num_array = [float(x) for x in array]
        for i in range(len(num_array)):
            if num_array[i] == int(num_array[i]):
                num_array[i] = int(num_array[i])
        return num_array
    except Exception:
        pass

    return array


def num_input(text: str) -> int:
    correct_input = False
    while not correct_input:
        try:
            num = int(input(text))
            return num
        except Exception:
            print("Введите число.")
            pass

def parse_two_nums(text: str) -> tuple[int, int] | tuple[str, int]:
    correct_input = False
    while not correct_input:
        try:
            user_input = input(text).split()
            if user_input[0] == 'q':
                return 'q', 0
            return int(user_input[0]), int(user_input[1])
        except Exception:
            print("Введите два числа через пробел")
            pass


def logger_setup():
    logging.config.dictConfig(LOGGING_CONFIG)

def main() -> None:
    """
    Точка входа в приложение
    :return: Данная функция ничего не возвращает
    """
    logger_setup()

    user_input = ""
    while True:
        goal = input("\nРад вас видеть! Зачем зашли? (в любой части программы напишите 'q', чтобы вернуться назад или выйти) \n1) Сортировать массив\n2) Потыкать структуры данных\n3) Проверить факториал и фибоначчи (поверьте, они работают)\n")
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
                            new_array = bubble_sort(list(array.copy()))
                        case "2":
                            new_array = bucket_sort(list(array.copy()))
                        case "3":
                            new_array = count_sort(list(array.copy()))
                        case "4":
                            new_array = HeapMax.heap_sort(list(array.copy()))
                        case "5":
                            new_array = quick_sort(list(array.copy()))
                        case "6":
                            flag = False
                            base = 10
                            while not flag:
                                base = num_input("Основание системы счисления (>= 2): ")
                                if base < 2:
                                    print("Основание системы счисления >= 2.")
                                else:
                                    flag = True
                            new_array = radix_sort(list(array.copy()), base)
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
                                logging.error(f"Algorithms results didn't coincides. Last algorithm: №f{user_input}")
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
                                        try:
                                            print(" - ", stack.pop())
                                        except(IndexError):
                                            logging.error("Attempted pop() to empty Stack")
                                            print("Стэк пуст.")
                                    case "2":
                                        x = num_input("Введите число: ")
                                        try:
                                            stack.push(x)
                                        except(IndexError):
                                            logging.error("Attempted push() to full Stack")
                                            print("Стэк переполнен.")
                                    case "3":
                                        try:
                                            print(" - ", stack.min())
                                        except(IndexError):
                                            logging.error("Attempted min() to empty Stack")
                                            print("Стэк пуст.")
                                    case "4":
                                        try:
                                            print(" - ", stack.peek())
                                        except(IndexError):
                                            logging.error("Attempted peek() to empty Stack")
                                            print("Стэк пуст.")
                                    case "5":
                                        print(" - ", len(stack)) # ?
                                    case "6":
                                        print(" - ", stack.body[:len(stack)])
                                    case "q":
                                        break

                        case "2":
                            max_size = num_input("Введите максимальный размер очереди: ")
                            queue = Queue(max_size)
                            print("Вы создали очередь. ")
                            while user_input != 'q':
                                user_input = input("\nВыберите действие:\n1) dequeue\n2) enqueue\n3) front\n4) len\n5) Посмотреть очередь\n")
                                match(user_input):
                                    case "1":
                                        try:
                                            print(" - ", queue.dequeue())
                                        except(IndexError):
                                            logging.error("Attempted dequeue() to empty Queue")
                                            print("Очередь пуста.")
                                    case "2":
                                        x = num_input("Введите число: ")
                                        try:
                                            queue.enqueue(x)
                                        except(IndexError):
                                            logging.error("Attempted enqueue() to full Queue")
                                            print("Очередь переполнена.")
                                    case "3":
                                        try:
                                            print(" - ", queue.front())
                                        except(IndexError):
                                            logging.error("Attempted front() to empty Queue")
                                            print("Очередь пуста.")
                                    case "4":
                                        print(" - ", len(queue))
                                    case "5":
                                        # Вывод очереди в правильном порядке
                                        if queue.is_empty():
                                            print(" - []")
                                        else:
                                            elements = []
                                            for i in range(len(queue)):
                                                elements.append(queue.body[(queue.head + i) % queue.max_size])
                                            print(" - ", elements)
                                    case "q":
                                        break
                        case "q":
                            break
            case "3":
                while True:
                    func_num, argument = parse_two_nums("\nВведите номер функции и числовой аргумент через пробел:\n1) Факториал\n2) Факториал (рекурсия)\n3) Фибоначчи\n4) Фибоначчи (рекурсия)\n")
                    match(func_num):
                        case 1:
                            try:
                                print(f"Результат: {argument}! = {factorial(argument)}")
                            except (ValueError):
                                logging.error("Attempted to take factorial of negative number")
                                print("Нельзя брать факториал отрицательного числа")
                        case 2:
                            try:
                                print(f"Результат: {argument}! = {factorial_resursive(argument)}")
                            except (RecursionError):
                                logging.error(f"Recursion depth exceed while calculating {argument}!")
                                print("Слишком большой аргумент.")
                            except (ValueError):
                                logging.error("Attempted to take factorial of negative number")
                                print("Нельзя брать факториал отрицательного числа")
                        case 3:
                            try:
                                print(f"{argument}-е число Фибоначчи = {fibo(argument)}")
                            except (ValueError):
                                logging.error("Attempted to calculate Fibonacci of negative index")
                                print("Числа Фибоначчи начинают индексироваться с 1")
                        case 4:
                            try:
                                print(f"{argument}-е число Фибоначчи = {fibo_resursive(argument)}")
                            except (RecursionError):
                                logging.error(f"Recursion depth exceed while calculating {argument}-го числа Фибоначчи")
                                print("Слишком большой аргумент.")
                            except (ValueError):
                                logging.error("Attempted to calculate Fibonacci of negative index")
                                print("Числа Фибоначчи начинают индексироваться с 1")
                        case 'q':
                            break
            case "q":
                break





if __name__ == "__main__":
    main()
