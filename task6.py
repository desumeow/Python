# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

subj = {}
with open('task6_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        lecture_int = re.findall(r'\d+', lecture)
        lecture_int = [int(i) for i in lecture_int]
        practice_int = re.findall(r'\d+', practice)
        practice_int = [int(i) for i in practice_int]
        lab_int = re.findall(r'\d+', lab)
        lab_int = [int(i) for i in lab_int]
        subj[subject] = sum(lecture_int + practice_int + lab_int)
    print(f'Общее количество часов по предмету - {subj}')