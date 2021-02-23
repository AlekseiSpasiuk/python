# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

lang_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

output_file = open("output4.txt", "w", encoding="utf-8")
input_file = open("./digit.txt", "r", encoding="utf-8")

for input_string in input_file:
    res = input_string.split()
    output_string = "\n"
    if res:
        output_string = lang_dict[res[0]]+" " + \
            " ".join(input_string.split()[1:])+"\n"
    output_file.write(output_string)

input_file.close()
output_file.close()
