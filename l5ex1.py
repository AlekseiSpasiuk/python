# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file = open('./output.txt', 'w', encoding="utf-8")
while True:
    text = input()
    if not text:
        break
    file.write(text + '\n')
file.close()
