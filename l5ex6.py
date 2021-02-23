# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def parce_line(line):
    from functools import reduce
    key, data = line.strip().split(":")[0], line.strip().split(" ")[1:]
    z = [x.strip().split("(")[0] for x in data if x.find("(") != -1]
    return (key, reduce(lambda a, b: a+int(b), z, 0)) #PS вот тут например применяется установленное значение в reduce :)


output = {}

with open("./inputl6.txt") as input:
    for line in input:
        a, b = (parce_line(line))
        output[a] = b
print(output)
