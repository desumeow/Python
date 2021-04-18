# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task2_file.txt', 'r', encoding='utf-8') as f:
    word_count=len(f.read().split())
    print(f'Количество слов в файле:{word_count}')
with open('task2_file.txt', 'r') as f:
    line_count = sum(1 for line in f)
    print(f'Количество строк в файле:{line_count}')
