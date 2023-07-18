# 5. Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.


import json

fi = 'task32.json'


class User:
    def __init__(self, name: str, id_user: int, access_level: int):
        self.name = name
        self.id_user = id_user
        self.access_level = access_level


    def __str__(self):
        return f'{self.name}, {self.id_user}, {self.access_level}'


    def __eq__(self, other):
        return self.name == other.name and self.id_user == other.id_user


    def __hash__(self):
        return hash((self.name, self.id_user))


    def json_reader(json_file: str) -> set[User]:
        with open(json_file, 'r', encoding='utf-8') as f:
            my_dict = json.load(f)
            users_set = set()
        for level, value in my_dict.items():
            for id_, name_ in value.items():
                users_set.add(User(name_, int(id_), int(level)))
        return users_set


if __name__ == '__main__':


# Создайте класс с базовым исключением и дочерние классы исключения:
# ошибка уровня,
# ошибка доступа.


class My_Exception(Exception):
    def __init__(self, value):
        self.value = value


class Level_Ecception(My_Exception):
    def __str__(self):
        return f'Произошла ошибка уровня. {self.value}: такой уровень не найден.'


class Access_Exception(My_Exception):
    def __str__(self):
        return f'Не верный уровень доступа.'


if __name__ == '__main__':
    raise Level_Ecception(4)