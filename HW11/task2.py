# 2. Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов,
# list-архивы также являются свойствами экземпляра.

class Archive:
    """
    Class Archive. При создании нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списков архивов.
    """

    _count = None

    def __new__(cls, *args, **kwargs):
        if cls._count is None:
            cls._count = super().__new__(cls)
            cls._count.list_num = []
            cls._count.list_str = []
        else:
            cls._count.list_num.append(cls._count.num)
            cls._count.list_str.append(cls._count.string)
        return cls._count

    def __init__(self, num, string):
        self.num = num
        self.string = string

    def __str__(self):
        return f"{self = } \n{self.num = } \n{self.string = }"


if __name__ == '__main__':
    a = Archive(4, 'q')
    print(a)
    print(a.__doc__)
    print(a.list_num)
    b = Archive(3, 'y')
    print(b.list_num)
    print(b.list_str)