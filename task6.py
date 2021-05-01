# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Warehouse:

    keeping = []
    fullness = 0
    id = 0

    def __init__(self, cap):
        self.capacity = int(cap)

    def __add__(self, other):
        if self.capacity == self.fullness:
            print('Склад заполнен')
        else:
            self.id += 1
            self.keeping.append({'ID':self.id, 'Name':other.name})
            self.fullness += 1

    def withdraw(self, pos, squad):
        print(f'{self.keeping[pos].get("Name")} отправлен в {squad}')
        self.keeping.pop(pos)
        self.fullness -= 1

class Office_Equip:

    def __init__(self, name, psize):
        self.name = name
        self.paper_size = psize

class Printer(Office_Equip):

    def __init__(self, name, psize, pspeed):
        Office_Equip.__init__(self, name, psize)
        self.print_speed = pspeed


class Scanner(Office_Equip):

    def __init__(self, name, psize, sspeed):
        Office_Equip.__init__(self, name, psize)
        self.scan_speed = sspeed

class Xerox(Office_Equip):

    def __init__(self, name, psize, xspeed):
        Office_Equip.__init__(self, name, psize)
        self.photocopying_speed = xspeed

def inp_speed_val(input):
    while True:
        try:
            speed = (input())
            if speed.isdigit() == False:
                raise ValueError()
            else:
                speed = int(speed)
                result = f'{speed} стр/мин'
                return result
        except ValueError:
            print('Введите корректное значение')

printer1 = Printer('Kyocera', 'A4', inp_speed_val(lambda : input('Введите скорость обработки страниц в минуту:')))
print(printer1.print_speed)