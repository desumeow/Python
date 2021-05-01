# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivision(Exception):

    txt = 'Делить на ноль нельзя'

    def __str__(self):
        return self.txt

class Num(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise ZeroDivision

        return Num(float(self) / float(other))

while True:
    try:
        dividend, divider = map(Num, input('Введите делимое и делитель через пробел:').split())
        print(dividend / divider)
    except ZeroDivision as z:
        print(z)
    except ValueError as v:
        print(v)
        break
