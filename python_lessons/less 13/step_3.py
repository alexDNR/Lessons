'''
    Is Valid Triangle?
Напишите функцию is_valid_triangle(side1, side2, side3), 
которая принимает в качестве аргументов три натуральных числа, и возвращает 
значение True если существует невырожденный треугольник со сторонами side1, side2, side3 
и False в противном случае.
Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора. (https://stepik.org/lesson/265083/step/12?unit=246031)
Примечание 2. Следующий программный код:
print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))

должен выводить:
True
False
True
'''
# # объявление функции
# def is_valid_triangle(side1, side2, side3):
#     if ((side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side1 + side2)):
#         return True
#     else:
#         return False   

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
# # вызываем функцию
# print(is_valid_triangle(a, b, c))


'''
    Is a Number Prime? 🌶️
Напишите функцию is_prime(num), которая принимает в качестве аргумента 
натуральное число и возвращает значение True если число является простым 
и False в противном случае.
Примечание. Следующий программный код:
print(is_prime(1))
print(is_prime(10))
print(is_prime(17))

должен выводить:
False
False
True
'''
# def is_prime(num):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2 and i != 1:
#         return True
#     else:
#         return False    

# # считываем данные
# n = int(input())
# # вызываем функцию
# print(is_prime(n))


'''
    Next Prime 🌶️🌶️
Напишите функцию get_next_prime(num), 
которая принимает в качестве аргумента натуральное число num 
и возвращает первое простое число большее числа num.
Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
Примечание 2. Следующий программный код:
print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))

должен выводить:
7
11
17
'''
# def is_prime(num):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2 and i != 1:
#         return True
#     else:
#         return False    

# # считываем данные
# n = int(input())
# # вызываем функцию
# while True:
#     n += 1
#     if is_prime(n):
#         print(n)
#         break
    

'''
    Good password 🌶️
Напишите функцию is_password_good(password), 
которая принимает в качестве аргумента строковое значение пароля password 
и возвращает значение True если пароль является надежным 
и False в противном случае.
Пароль является надежным если:
- его длина не менее 8 символов; 
- он содержит как минимум одну заглавную букву (верхний регистр); 
- он содержит как минимум одну строчную букву (нижний регистр);
- он содержит хотя бы одну цифру.
Примечание. Следующий программный код:
print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))

должен выводить:
True
False
'''
# # объявление функции
# def is_password_good(password):
#     lower = 0
#     upper = 0
#     digit = 0
#     if len(password) >= 8:
#         for i in password:
#             if i.islower():
#                 lower += 1
#             if i.isupper():
#                 upper += 1
#             if i.isdigit():
#                 digit += 1
#         if lower >= 1 and upper >= 1 and digit >= 1:
#             return True
#         else:
#             return False                    
#     else:
#         return False

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_password_good(txt))


'''
    Ровно в одном
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов 
два слова word1 и word2 и возвращает значение True если слова имеют одинаковую длину 
и отличаются ровно в 1 символе и False в противном случае.
Примечание. Следующий программный код:
print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))

должен выводить:
True
True
False
False
'''
# # объявление функции
# def is_one_away(word1, word2):
#     not_similar = 0
#     if len(word1) != len(word2):
#         return False
#     else:
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 not_similar += 1
#         if not_similar == 1:
#             return True
#         else:
#             return False            
# # # считываем данные
# txt1 = input()
# txt2 = input()
# # # # вызываем функцию
# print(is_one_away(txt1, txt2))


'''
    Палиндром 🌶️
Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку 
text и возвращает значение True если указанный текст является палиндромом и 
False в противном случае.
Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, 
а также игнорируйте пробелы, а также символы , . ! ? -.
Примечание 3. Следующий программный код:
print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))

должен выводить:
True
True
False
'''
# # объявление функции
# def is_palindrome(text):
#     text = ''.join(i.lower() for i in text if i.isalpha())
#     if text[::] == text[::-1]:
#         return True
#     else:
#         return False    
# # считываем данные
# txt = input()
# # вызываем функцию
# print(is_palindrome(txt))


'''
    BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы 
с необычным паролем.
Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. 
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
- число a – должно быть палиндромом;
- число b – должно быть простым;
- число c – должно быть четным.
Напишите функцию is_valid_password(password), 
которая принимает в качестве аргумента строковое значение пароля password 
и возвращает значение True если пароль является действительным паролем 
BEEGEEK банка и False в противном случае.
Примечание. Следующий программный код:
print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:
True
False
False
False
'''
# # объявление функции палиндрома
# def is_palindrome(num):
#     text = str(num)
#     if text[::] == text[::-1]:
#         return True
#     else:
#         return False  
# # объявление функции чётности числа 
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False    
# # объявление функции простого числа
# def is_prime(num):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2 and i != 1:
#         return True
#     else:
#         return False 
# # объявление функции
# def is_valid_password(password):
#     password = [int(i) for i in password.split(':')]  
#     if len(password) == 3:
#         if is_palindrome(password[0]) and is_prime(password[1]) and is_even(password[2]):
#             return True
#         else:
#             return False    
#     else:
#         return False

# # считываем данные
# psw = input()
# # вызываем функцию
# print(is_valid_password(psw))


'''
    Правильная скобочная последовательность 🌶️
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента 
непустую строку text, состоящую из символов ( и ) и возвращает значение True 
если поступившая на вход строка является правильной скобочной последовательностью и 
False в противном случае.
Примечание 1. Правильной скобочной последовательностью называется строка, 
состоящая только из символов ( и ), где каждой открывающей скобке 
найдется парная закрывающая скобка.
Примечание 2. Следующий программный код:
print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))

должен выводить:
True
False
'''
# # объявление функции
# def is_correct_bracket(text):
#     while '()' in text:        
#         text = text.replace('()', '')
#         if len(text) == 0:
#             break
#     print(text)
#     if len(text) == 0:
#         return True
#     else:
#         return False
# # считываем данные
# txt = input()
# # вызываем функцию
# print(is_correct_bracket(text))


'''
    Змеиный регистр
Напишите функцию convert_to_python_case(text), 
которая принимает в качестве аргумента строку в «верблюжьем регистре» и 
преобразует его в «змеиный регистр».
Примечание 1. Почитать подробнее о стилях именования можно тут.
Примечание 2. Следующий программный код:
print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))

должен выводить:
this_is_camel_cased
is_prime_number
'''
# # объявление функции
# def convert_to_python_case(text):
#     s = text[0].lower()
#     for i in range(1, len(text)):
#         if text[i].islower():
#             s = s + text[i]
#         elif text[i].isupper():
#             s = s + '_' + text[i].lower() 
#         else:
#             s = s + text[i]       
#     return s              
# # считываем данные
# txt = input()
# # вызываем функцию
# print(convert_to_python_case(txt))


'''
Середина отрезка
Напишите функцию get_middle_point(x1, y1, x2, y2), 
которая принимает в качестве аргументов координаты концов отрезка 
(x_1; y_1)(x_2; y_2) и возвращает координаты точки являющейся 
серединой данного отрезка.
Примечание 1. Координаты середины отрезка вычисляются по формуле:
(x1+x2)/2;(y1+y2)/2  
'''
# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     x = (x1+x2)/2
#     y = (y1+y2)/2
#     return x,y
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


'''
    Площадь и длина
Напишите функцию get_circle(radius), которая принимает в качестве аргумента 
радиус окружности и возвращает два значения: длину окружности и площадь круга, 
ограниченного данной окружностью.
Примечание 1. Длина окружности и площадь круга радиуса rr вычисляются по формулам:
С=2πr,S=πr^2.
Примечание 2. Для числа π используйте глобальную константу из модуля math.
Примечание 3. Следующий программный код:
print(get_circle(1))
print(get_circle(1.5))

должен выводить:
6.283185307179586 3.141592653589793
9.42477796076938 7.0685834705770345
'''
# from math import*
# # объявление функции
# def get_circle(radius):
#     c = 2*pi*radius
#     s = pi * radius**2
#     return c,s
# # считываем данные
# r = float(input())
# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)


'''
    Корни уравнения 🌶️🌶️
Напишите функцию solve(a, b, c), которая принимает в качестве аргументов 
три целых числа a, b, c – коэффициенты квадратного уравнения ax^2+bx+c = 0 
и возвращает его корни в порядке возрастания.
Примечание 1. С подобной задачей мы уже сталкивались. https://stepik.org/lesson/265110/step/7?unit=246058
Примечание 2. Гарантируется, что квадратное уравнение имеет корни.
Примечание 3. Следующий программный код:
print(solve(1, -4, -5))
print(solve(-2, 7, -5))
print(solve(1, 2, 1))

должен выводить:
-1.0 5.0
1.0 2.5
-1.0 -1.0
'''
# from math import *
# # объявление функции
# def solve(a, b, c):
#     d = b**2 - 4*a*c
#     if d > 0:
#         x1 = (-b + sqrt(d))/(2*a)
#         x2 = (-b - sqrt(d))/(2*a)
#         kor_1 = min(x1, x2)
#         kor_2 = max(x1, x2)
#         return kor_1, kor_2 
#     elif d == 0:
#         x1 = x2 = -(b/(2*a))
#         return x1, x2    
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)