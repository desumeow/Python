# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import time

class Date:

    def __init__(self, month, day, year):
        self.date_inp = f'{month}-{day}-{year}'

    @classmethod
    def int_convert(cls, date_inp):
        int_date = []

        for i in date_inp.split('-'):
            int_date.append(int(i))

        return int_date[0], int_date[1], int_date[2]

    @staticmethod
    def date_val(date_inp):
        int_date = []
        errors = []
        try:
            time.strptime(date_inp, '%m-%d-%Y')
            return 'Всё в порядке'
        except Exception as e:
            raise e


day = Date(2, 23, 2021)
print(day.date_inp)
print(Date.int_convert(day.date_inp))
print(day.date_val(day.date_inp))
day2 = Date(2, 30, 2021)
print(day2.date_inp)
print(Date.int_convert(day2.date_inp))
print(day2.date_val(day2.date_inp))
