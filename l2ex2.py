#!python3

# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
count = 0
iList = list()
print('enter to exit or ctrl+d')
while(True):
    try:
        iList.append(input(f'input {count} element: '))
        count += 1
        if iList[-1] in (''):
            iList.pop()
            break
    except EOFError: # исключение для обработки ctr+d или перенаправления ввода cat test | ./l2ex2.py
        break
print('\n\n','input List = ',iList)
for count in range(len(iList))[1::2]:
    print(count,count-1)
    iList[count-1],iList[count] = iList[count],iList[count-1]

print('output List = ',iList)

