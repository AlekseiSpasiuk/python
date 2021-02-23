# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def generate_string():
    from random import randint
    return " ".join([str(randint(1, x)) for x in range(1, 100, 1)])


with open("./input5.txt", "w", encoding="utf-8") as output_file:
    output_file.write(generate_string())

with open("./input5.txt", "r", encoding="utf-8") as input_file:
    from functools import reduce
    print(reduce(lambda a, b: a+int(b), input_file.read().split(" "), 0))
