# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки,также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json


def init_average():
    sum = 0
    count = 0

    def add_sum(x):
        nonlocal count
        nonlocal sum
        sum += x
        count += 1

    def get_average():
        return {"average_profit": sum / count}
    return add_sum, get_average


def parce_line(line):
    res = line.strip().split()
    return res[0], int(res[2])-int(res[3])


add, result = init_average()
struct = {}
with open("./firms.txt", "r", encoding="utf-8") as input_file:
    for line in input_file:
        key, profit = parce_line(line)
        struct[key] = profit
        if profit > 0:
            add(profit)
with open("output7.json", "w") as out:
    json.dump([struct, result()], out)
