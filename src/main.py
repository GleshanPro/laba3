from src.factorial import factorial
from src.factorial import factorial_resursive

from src.fibonacci import fibo
from src.fibonacci import fibo_resursive



def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    num = int(input("Введите число: "))

    result = fibo(num)
    # result1 = factorial(num)
    # result2 = factorial_resursive(num)

    print(result)

if __name__ == "__main__":
    main()
