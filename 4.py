#Пользователь вводит целое положительное число.
#Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

innum = int(input('Введите число:'))
result = -1
while innum > 10:
    a = innum % 10
    innum //= 10
    if a > result:
        result = a
print(f'Результат:{result}')
