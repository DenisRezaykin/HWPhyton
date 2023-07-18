# 3. Создайте класс с базовым исключением и дочерние классы-исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class BaseException(Exception):
    pass


class LevelException(BaseException):
    def __str__(self) -> str:
        return "Ошибка уровня"


class AccessException(BaseException):
    def __str__(self) -> str:
        return 'Ошибка доступа'


if __name__ == '__main__':
    raise LevelException