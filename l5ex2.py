# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
file_input = open("LICENSE", "r", encoding="utf-8")
count_string = 0
count_word_in_string = 0
for file_string in file_input:
    count_string += 1
    count_word_in_string = len(file_string.split())
    print(file_string, count_string, count_word_in_string)
file_input.close()
