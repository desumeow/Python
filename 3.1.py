#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.
#seasons = {1:'winter', 2:'winter', 12:'winter',
#           3:'spring', 4:'spring', 5:'spring',
#           6:'summer', 7:'summer', 8:'summer',
#           9:'autumn', 10:'autumn', 11:'autumn'}
#Вариант №1
#monthnum = int(input('Enter the month number - '))
#for key in seasons:
#    if monthnum == key:
#        print(f'This month refers to {seasons.get(key)}')

#Вариант №2 с таким словарем
#monthnum = int(input('Enter the month number - '))

#print(f'This month refers to {seasons.get(monthnum)}')



seasons = {'winter':[1, 2, 12],
           'spring':[3, 4, 5],
           'summer':[6, 7, 8],
           'autumn':[9, 10, 11]}

monthnum = int(input('Enter the month number - '))

index = 0
#Вариант №3
for value in seasons.values():
    if monthnum in value:
        key_list = list(seasons)
        print(f'This month refers to {key_list[index]}')
        break
    index += 1

#Вариант №4
#for win in seasons['winter']:
#    if monthnum == win:
#        print(f'This month refers to winter')
#
#for spr in seasons['spring']:
#    if monthnum == spr:
#        print('This month refers to spring')
#
#for summ in seasons['summer']:
#    if monthnum == summ:
#        print('This month refers to summer')
#
#for aut in seasons['autumn']:
#    if monthnum == aut:
#        print('This month refers to autumn')

if monthnum >= 13:
    print('Invalid number')