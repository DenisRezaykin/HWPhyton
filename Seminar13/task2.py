# 2. Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def get(my_dict, my_key, default_value = 5):
    try:
        res = my_dict[my_key]
    except KeyError as e:
        print(f'There is no such key {my_key} in dictionary')
        print(f'Set default value {default_value}')
    res = default_value
    return res


if __name__ == "__main__":
    my_dict = {1: 3, 2: 4}
    print(get(my_dict, 3))