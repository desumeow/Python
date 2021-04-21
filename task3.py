# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    name = 'Иван'
    surname = 'Иванов'
    position = 'Работяга'
    _income = {'Оклад':16000, 'Премия':5000}


class Position(Worker):

    def get_full_name(self):
        print(Position.name + ' ' + Position.surname)

    def get_total_income(self):
        print(sum(Position._income.values()))

vasyan = Position()
vasyan.get_full_name()
vasyan.get_total_income()