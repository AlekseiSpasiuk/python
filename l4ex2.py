#!python3

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint

def check_init(x):
    z = x
    def check(x):
        nonlocal z
        out = False
        if x > z:
            out = True
        z = x
        return out
    return check

l = [randint(1, 10) for x in range(10)]
check = check_init(l[0])
print(f"original list -> {l}")
print(f'output list -> {list(filter(check,l))}')
