# 4. Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json


class User:
    def __init__(self, name: str, user_id: int, level: int) -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self) -> str:
        return f"User: {self.name}, id: {self.user_id}, level: {self.level}"


def get_users(file_json: str) -> set[User]:
    user_data = None
    with open(file_json, mode="r", encoding="utf-8") as f:
        user_data = json.load(f)
    users = [User(user["name"], user["id"], user["level"]) for user in user_data]
    return set(users)


if __name__ == '__main__':
    u = User('q', 1, 3)
    for user in get_users('data2.json'):
        print(user)