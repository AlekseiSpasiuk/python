#!python3

# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

array = []
array.append(None)
array.append(123)
array.append('hello, world!')
array.append((11,22,33))
array.append({1,2,3,4,5,6,7,8,9,0})
array.append({'a':10,'b':20,'c':30})
array.append(list(range(10)))
print(array)
for element in array:
    print(element, type(element), sep=' -> ')
