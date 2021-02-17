#!python3

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(a:int, b:int) -> float:
    if not b:
        print("division by zero")
    else:
        return a / b
a = int(input("a = "))
b = int(input("b = "))

c = division(a,b)
if c:
    print(c)

