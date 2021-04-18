# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("task5_file.txt", "w", encoding='utf-8') as f:
    f.write(input('Введите числа через пробел:'))
with open("task5_file.txt", "r", encoding='utf-8') as f:
    for i in f:
        r = i.strip().split()
        result = map(int, r)
        print(sum(result))