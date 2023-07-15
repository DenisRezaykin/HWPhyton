# 1. Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)


from time import time


class MyStr(str):
    """Class MyStr. Дополнительно хранятся имя автора строки и время создания."""

    def __new__(cls, autor, value):
        instance = super().__new__(cls, value)
        instance.autor = autor
        instance.time = time()
        return instance

    def __str__(self):
        return f"{self = } \n{self.autor = } \n{self.time = }"


a = MyStr("George", "string123")
print(a)
print(a.upper())
print(a.autor)
# help(MyStr)
print(MyStr.__doc__)