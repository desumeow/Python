# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:

    keeping = []
    fullness = 0

    def __init__(self, cap):
        self.capacity = int(cap)

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

