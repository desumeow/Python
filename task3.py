# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.

class ControlError(Exception):

    def __init__(self, txt):
        self.txt = txt

def contr(lst):
    if len(lst) == 0:
        return 'Список пустой'
    else:
        try:
            for i in lst:
                if i.isdigit() == False:
                    raise ControlError('В списке не только числа.')
        except ControlError as c:
            return c
        else:
            return 'В списке только числа.'

inp_data = []
ex = True

while ex:
    datain = input('Введите числа через пробел, либо stop для завершения работы:')
    for it in datain.split():
        if it.upper() == 'STOP':
            ex = False
            break
        else:
            inp_data += it.split()
    if ex == False:
        print(inp_data)
        print(contr(inp_data))
