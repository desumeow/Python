#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы.
#Реализовать вывод данных о пользователе одной строкой.

def my_func(fname = 'Имя', surname = 'Фамилия', byear = 'Год рождения', city = 'Город', email = 'email', phone = 'телефон'):
    return (fname, surname, byear, city, email, phone)

print(my_func('Иван', 'Иванович', '1989', 'Омск', 'почта', '+5666594294907'))
