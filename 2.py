# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

import time
sec = int(input('Введите количество секунд - '))
result = time.strftime('%H:%M:%S', time.gmtime(sec))
print(f'Результат: {result}')