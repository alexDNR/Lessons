# # объявление функции
# def draw_box():
#     print('*'*10)
#     for _ in range(12):
#         print('*        *')
#     print('*'*10)
# # основная программа
# draw_box()  # вызов функции


# # объявление функции
# def draw_triangle():
#     for i in range(10+1):
#         print('*'*i)
# # основная программа
# draw_triangle()  # вызов функции


# def print_number(a, b, c):
#     d = (a + c) // b
#     print(d)

# print_number(2, 3, 11)    


# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
# x = 1
# y = 7
# print(x, y)
# change_us(x, y)
# print(x, y)


'''
    Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
- fill – символ заполнитель;
- base – величина основания равнобедренного треугольника;
а затем выводит его.
Примечание. Гарантируется, что основание треугольника – нечетное число.
'''
# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(base//2 + 1):
#         for j in range(i + 1):
#             print(fill, end="")
#         print()    
#     for i in range(base//2, 0, -1):
#         for j in range(i):
#             print(fill, end="")
#         print()
# # считываем данные
# fill = input()
# base = int(input())
# # вызываем функцию
# draw_triangle(fill, base)    


'''
    ФИО
Напишите функцию print_fio(name, surname, patronymic), 
которая принимает три параметра:
- name – имя человека;
- surname – фамилия человека;
- patronymic – отчество человека;
а затем выводит на печать ФИО человека.
Примечание. Предусмотрите тот факт, что все три буквы в ФИО 
должны иметь верхний регистр.
'''
# # объявление функции
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')

# # считываем данные
# name, surname, patronymic = input(), input(), input()
# # вызываем функцию
# print_fio(name, surname, patronymic)


'''
Сумма цифр
Напишите функцию print_digit_sum(), 
которая принимает одно целое число num и выводит на печать сумму его цифр.
'''
# # объявление функции
# def print_digit_sum(num):
#     total = 0
#     while num != 0:
#         total += num % 10
#         num //= 10
#     print(total)    
# # считываем данные
# n = int(input())

# # вызываем функцию
# print_digit_sum(n)