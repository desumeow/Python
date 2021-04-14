# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def processInput(input):
    while True:
         try:
             result = float(input());
             if result < 0:
                 raise ValueError()
             return result
         except ValueError:
             print('Введите корректное значение')

def salary(work, rate, prize):
    result = round(((work * rate) + prize), 2)
    return (f'Ваша зарплата равна {result}')

work = processInput(lambda: input('Введите выработку в часах:'))
rate = processInput(lambda: input('Введите ставку в час:'))
prize = processInput(lambda: input('Введите премию:'))

print(salary(work, rate, prize))

