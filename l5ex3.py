# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
def check_input(input_string):
    if not input_string:
        return False
    output = list(map(lambda a: a.strip(), input_string.split(";")))
    if len(output) != 2 or not output[1].isdigit():
        return False
    return [output[0], int(output[1])]


def print_rule(workers):
    for worker in workers:
        if worker[1] < 20000:
            print(worker[0])


def print_average(workers):
    sum = 0
    for zp in workers:
        sum += zp[1]
    print(f"average = {sum/len(workers)}")


workers = []

with open("./zp.csv", "r", encoding="utf-8") as zp:
    for line in zp:
        workers.append(check_input(line))

workers = list(filter(None, workers))
print_rule(workers)
print_average(workers)
