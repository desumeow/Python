# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file_create = open("task1_file.txt", "w", encoding='utf-8')
while True:
    with open("task1_file.txt", "a") as f:
        datain = input('Введите текст, либо нажмите enter для выхода:')
        if datain == '':
            print('Завершение работы.')
            break
        else:
            f.writelines(datain + '\n')