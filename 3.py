#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.
lst_win = [12, 1, 2]
lst_sum = [6, 7, 8]
lst_spr = [3, 4, 5]
lst_aut = [9, 10, 11]
monthnum = int(input('Enter the month number - '))
for win in lst_win:
    if win == monthnum:
        print('Этот месяц относится к зиме')

for spr in lst_spr:
    if spr == monthnum:
        print('Этот месяц относится к весне')

for sum in lst_sum:
    if sum == monthnum:
        print('Этот месяц относится к лету')

for aut in lst_aut:
    if aut == monthnum:
        print('Этот месяц относится к осени')
if monthnum >= 13:
    print('Invalid number')
