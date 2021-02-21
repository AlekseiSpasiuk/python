#!python3

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def calculate_zp(working_time:float, money_to_house:float, premium:float)->float:
    return working_time * money_to_house + premium

print(calculate_zp(*map(float,argv[1:])))

