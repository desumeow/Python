# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from statistics import mean

with open('task3_file.txt', 'r', encoding='utf-8') as f:
    salaries = []
    for worker in f:
        last_name, salary = worker.split()
        salary = int(salary)
        if salary < 20_000:
            print(f'{last_name} - зарплата меньше 20к')
        salaries.append(salary)
    print(mean(salaries))
