#Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
        return sum((a, b, c)) - min(a, b, c)



try:
    a = float(input('Введите первое число:'))
    b = float(input('Введите второе число:'))
    c = float(input('Введите третье число:'))
    print(my_func(a, b, c))
except ValueError:
        print('Введите число.')