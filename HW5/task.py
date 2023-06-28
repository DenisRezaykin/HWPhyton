# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def absolute_path(path: str) -> tuple:
    file_name = path.split("/")[-1]
    file_extension = file_name.split('.')[1]
    result = path, file_name, file_extension
    return result


path = 'C:/Users/George/Downloads/Lessons/file.txt'
print(absolute_path(path))

# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии.


names = ['George', 'Kevin', 'Diana']
salaries = [50_000, 70_000, 40_000]
bonuses = ['10.25%', '15.15%', '8.75%']

dict_ = {names[i]: (salaries[i] * float(bonuses[i].split('%')[0]) / 100) for i in range(3)}
print(dict_)


# Создайте функцию генератор чисел Фибоначчи.


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


print(*fibonacci(10))
