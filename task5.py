# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

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

sklad_1 = Warehouse(2)
printer1 = Printer('Kyocera', 'A4', '20 стр/мин')
sklad_1 + printer1
sklad_1 + printer1
sklad_1 + printer1
print(sklad_1.fullness)
print(sklad_1.keeping)
sklad_1.withdraw(1, '30 отдел')
print(sklad_1.keeping)
sklad_1 + printer1
print(sklad_1.keeping)