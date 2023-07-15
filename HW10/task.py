# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animals:
    def __init__(self, name, tail):
        self.name = name
        self.tail = tail

    def name_animal(self):
        return self.name


class Fish(Animals):
    def __init__(self, fresh_water, deep, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fresh_water = fresh_water
        self.deep = deep

    def specific(self):
        if self.fresh_water:
            return True
        return False

    def check_deep(self):
        if self.deep <= 3:
            return f"Мелководное до {self.deep} метров"
        elif 3 < self.deep < 20:
            return f"Среднеглубинное до {self.deep} метров"
        return f"Глубоководное глубже {self.deep} метров"


class Birds(Animals):

    def __init__(self, wingspan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wingspan = wingspan

    def specific(self):
        wing_lengh = self.wingspan * 0, 45
        return wing_lengh


class Mammals(Animals):

    def __init__(self, hibernate, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hibernate = hibernate

    def specific(self):
        if self.hibernate:
            return True
        return False


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == "Fish":
            return Fish(**kwargs)
        elif animal_type == "Birds":
            return Birds(**kwargs)
        elif animal_type == "Mammals":
            return Mammals(**kwargs)
        else:
            raise ValueError("Invalid animal type")


fish_params = {"name": "Salmon", "tail": True, "fresh_water": True, "deep": 5}
fish = AnimalFactory.create_animal("Fish", **fish_params)

bird_params = {"name": "Eagle", "tail": False, "wingspan": 2.5}
bird = AnimalFactory.create_animal("Birds", **bird_params)

mammal_params = {"name": "Bear", "tail": True, "hibernate": True}
mammal = AnimalFactory.create_animal("Mammals", **mammal_params)


# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.
import os
from random import randint, uniform
from pathlib import Path


class Fill_file:
    minim = -1000
    maxim = 1000

    def __init__(self, name, quanty, directory):
        self.name = name
        self.quanty = quanty
        self.dir = directory

    def generate(self):
        Path(self.dir).mkdir(parents=True, exist_ok=True)
        path_to_files = Path(self.dir) / self.name
        with open(f'{path_to_files}', 'a+', encoding='utf-8') as f:
            for _ in range(self.quanty):
                print(f'{str(randint(Fill_file.minim, Fill_file.maxim))}|'
                      f'{str(uniform(Fill_file.minim, Fill_file.maxim))}', file=f)


if __name__ == "__main__":
    sample = Fill_file('result_1.txt', 100, os.getcwd())
    sample.generate()