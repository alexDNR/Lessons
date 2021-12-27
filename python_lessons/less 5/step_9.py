'''
    Цветовой микшер 🌶️
Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов. 
При смешивании двух основных цветов получается вторичный цвет:
---
если смешать красный и синий, то получится фиолетовый;
если смешать красный и желтый, то получится оранжевый;
если смешать синий и желтый, то получится зеленый.
---
Напишите программу, которая считывает названия двух основных цветов для смешивания. 
Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке. 
В противном случае программа должна вывести название вторичного цвета, который получится в результате.

    Формат входных данных
На вход программе подаются две строки, каждая на отдельной строке.

    Формат выходных данных
Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.

Примечание 1. Если смешать красный и красный, то получится красный и т.д.
Примечание 2. Поиграйтесь с настоящим цветовым микшером 🙂 https://colorscheme.ru/color-names.html
'''
f_c = str(input())
s_c = str(input())
if (f_c == 'красный') or (f_c == 'синий') or (f_c == 'желтый'):
    if (s_c == 'красный') or (s_c == 'синий') or (s_c == 'желтый'):
        if (f_c == 'красный') and (s_c == 'красный'):
            print('красный')
        elif (f_c == 'синий') and (s_c == 'синий'): 
            print('синий')
        elif (f_c == 'желтый') and (s_c == 'желтый'): 
            print('желтый') 
        elif ((f_c == 'красный') and (s_c == 'синий')) or ((f_c == 'синий') and (s_c == 'красный')): 
            print('фиолетовый') 
        elif ((f_c == 'красный') and (s_c == 'желтый')) or ((f_c == 'желтый') and (s_c == 'красный')): 
            print('оранжевый')  
        elif ((f_c == 'синий') and (s_c == 'желтый')) or ((f_c == 'желтый') and (s_c == 'синий')): 
            print('зеленый')  
    else:
        print("ошибка цвета")                                 
else:
    print("ошибка цвета")    

# урок пройден