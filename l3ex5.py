#!python3

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

ch = 'q'
out_sum = 0

def list_sum(l : list, foo = lambda a, b : a + b) -> int:
    """Сумирование элементов списка, аналог reduce()"""
    a = 0
    for i in l:
        a = foo(a, i)
    return a

print(f"input {ch} to exit")
while(True):
    flag = False
    input_string = input('you string = ')
    if ch in input_string:
        flag = True
        input_string = input_string[:input_string.find(ch)].strip()
    l = list(map(int,input_string.split(" ")))
#    print(f"{l} -> {list_sum(l)}") # для проверки))
    out_sum += list_sum(l)
    print(f"sum = {out_sum}")
    if flag:
        break
