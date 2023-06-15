# Напишите код, который запрашивает число и сообщает, является ли оно
# простым или составным. Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MAX_INPUT_NUMBER = 100000


def detect_simple(num):  # Функция определения простого числа
    if num % 2 == 0:  # Простые числа ВСЕ нечетные, кроме 2
        return num == 2
    d = 3
    while d * d <= num and num % d != 0:  # Делитель не может превышать значение
        # квадратного корня из n
        d += 2  # Увеличиваем делитель на 2, т.к. четных делителей быть не должно
    return d * d > num


if __name__ == '__main__':
    n = int(input("Введите число: "))

    if (n < 0) or (n > MAX_INPUT_NUMBER):
        print(f"Вводите целые числа больше 0 и меньше {MAX_INPUT_NUMBER}")
    else:
        print(f"Число {n} - {'простое' if detect_simple(n) else 'составное'}")

# Результат работы:
# C:\Work\python\dz3\Py3HW01\venv\Scripts\python.exe C:/Work/python/dz3/Py3HW01/task02.py
# Введите число: 31
# Число 31 - простое
#
# C:\Work\python\dz3\Py3HW01\venv\Scripts\python.exe C:/Work/python/dz3/Py3HW01/task02.py
# Введите число: 34
# Число 34 - составное
#
# Process finished with exit code 0
