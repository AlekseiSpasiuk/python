#!python3

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и через dict.

winter = [12,1,2]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
seasons = {"Зима":winter, "Весна":spring, 'Лето':summer, 'Осень':autumn}

numMonth = int(input("Введите номер месяца: "))

# решение через списки
if numMonth in winter:
    print('Зима')
elif numMonth in spring:
    print('Весна')
elif numMonth in summer:
    print('Лето')
elif numMonth in autumn:
    print('Осень')

# решение через словарь

for key, values in seasons.items():
    if numMonth in values:
        print(key)
