# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    title = 'канцелярская принадлежность'

    def draw():
        print('Канцелярская принадлежность лежит')

class Pen(Stationery):

    def draw():
        print('Ручка пишет')

class Pencil(Stationery):

    def draw():
        print('Карандаш чертит')

class Handle(Stationery):

    def draw():
        print('Маркер кончился')

stepler = Stationery
stepler.draw()

rychka = Pen
rychka.draw()

karandash = Pencil
karandash.draw()

marker = Handle
marker.draw()