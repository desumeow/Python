# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
import random

class Car:

    speed = None
    color = None
    name = None
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.color.capitalize()} {self.name.lower()} поехал')
        self.speed = random.randint(1, 80)

    def stop(self):
        print(f'{self.color.capitalize()} {self.name.lower()} остановился')
        self.speed = f'{self.color.capitalize()} {self.name.lower()} стоит'

    def show_speed(self):
        if isinstance(self.speed, int):
            print(f'{self.color.capitalize()} {self.name.lower()} двигается со скоростью {self.speed} км/ч')
        else:
            print(self.speed)

    def turn(self, direction):
        print(f'{self.color.capitalize()} {self.name.lower()} едет {direction}')

class TownCar(Car):

    def show_speed(self):
        if isinstance(self.speed, int):
            print(f'{self.color.capitalize()} {self.name.lower()} двигается со скоростью {self.speed}')
            if self.speed > 60:
                print(f'{self.color.capitalize()} {self.name.lower()} превышает скорость')
        else:
            print(self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if isinstance(self.speed, int):
            print(f'{self.color.capitalize()} {self.name.lower()} двигается со скоростью {self.speed}')
            if self.speed > 40:
                print(f'{self.color.capitalize()} {self.name.lower()} превышает скорость')
        else:
            print(self.speed)

class PoliceCar(Car):

    is_police = True

koen = SportCar('белый', 'koenigsegg regera')
koen.go()
koen.show_speed()

logan = TownCar('синий', 'renault logan')
logan.go()
logan.show_speed()
logan.stop()
logan.show_speed()

kamaz = WorkCar('зеленый', 'kamaz-6580')
kamaz.go()
kamaz.show_speed()

police = PoliceCar('полицейский', 'ford crown victoria')
police.go()
police.show_speed()
police.turn('направо')
police.stop()
police.show_speed()