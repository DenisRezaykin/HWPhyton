# Напишите функцию для транспонирования матрицы
import numpy as np
matrix = [[1, 2], [31, 4], [17, 15], [20, 48]]

def my_func (mat):
    zip_matrix = zip(*mat)
    transpon_matrix = [list(row) for row in zip_matrix]
    return transpon_matrix

def my_func2 (mat):
    arr_matrix = np.array(mat)
    transpon_matrix2 = arr_matrix.transpose()
    return transpon_matrix2

print(matrix)
print(my_func(matrix))
print(my_func2(matrix))

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

# *args
# hash

def my_func (**kwargs):
    for _ in kwargs:
        kwargs = dict(reversed(item) for item in kwargs.items())
        return kwargs

def my_func2 (**kwargs):
    for _ in kwargs:
        kwargs2 = {v: k for k, v in kwargs.items()}
        return kwargs2

print(my_func(a = 0, b =1, c = 3, d = 4))
print(my_func2(a = 0, b =1, c = 3, d = 4))

# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.
import sys

BALANCE = 0
MIN = 50
MAX = 5_000_000
RATE = 0.015
BONUSRATE = 0.03
COUNT = 0
TAX = 0.1
def add_money():
    global COUNT, BALANCE
    money = int(input('Введите сумму пополнения, кратную 50 у.е.'))
    if money % 50 == 0:
        BALANCE += money
        print(f'Вы пополнили счет на {money} у.е. ')
        COUNT += 1.
    else:
        print('Сумма пополнения не кратно 50 у.е.')

def add_bonus():
    global BONUSRATE, BALANCE
    BONUSSUM = BALANCE * BONUSRATE
    BALANCE += BALANCE * BONUSRATE
    print(f'начислен бонус {BONUSSUM}')

def get_money() -> int:
    global COUNT, BALANCE, RATE
    money = int(input('Введите сумму снятия, кратную 50 у.е.'))
    if money > BALANCE:
        print('Запрашиваемая сумма, больше чем сумма на счете')
    elif money % 50 == 0:
        if money * RATE < 30:
            rate = 30
        elif money * RATE > 600:
            rate = 600
        else:
            rate = money * RATE
        BALANCE = BALANCE - money - rate
        print(f'Вы сняли со счета {money} и проценты за снятие {rate} у.е.')
        COUNT += 1
    else:
        print('Сумма снятия не кратна 50 у.е.')


while True:
    print(f'Cумма на счету составляет {BALANCE} у.е.')
    print('Выберите действие:\n\
1 - пополнить\n\
2 - снять\n\
3 - выйти')
    choise = input("Введите цифру: ")
    if BALANCE > MAX:
        TAXE = BALANCE * TAX
        BALANCE -= TAXE
        print(f'С вас списали налог на богатство в размере {TAXE}')

    match choise:
        case '1':
            add_money()
            #print(f'Cумма на счету составляет {card.BALANCE} у.е.')
        case '2':
            get_money()
            #print(f'Cумма на счету составляет {card.BALANCE} у.е.')
        case '3':
            sys.exit()

    if COUNT % 3 == 0:
        add_bonus()
    else:
        pass
