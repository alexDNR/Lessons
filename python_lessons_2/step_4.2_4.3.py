'''
Вложенные списки
'''
# list1 = [[0, [9, 2]], [1, [4, 6, 3], [5, 2, 3], 8, 3]]
# print(list1[1])
# print(list1[1][2])
# print(list1[1][2][1])

# list1 = [[1, 8, 7, 4], [1, 3, 4, 5, 6], [2, 7, 2], [2, 6, 7, 8]]
# print(max(list1))
'''
Дополните приведенный код, используя списочный метод append(), чтобы список list1 имел вид:
list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
'''
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
'''
Дополните приведенный код, используя списочный метод extend(), чтобы список list1 имел вид:
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
Подсписок для расширения  sub_list = ['h', 'i', 'j']
'''
# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)
'''
Дополните приведенный код, используя цикл for и встроенную функцию max(), 
чтобы он выводил один общий максимальный элемент 
среди всех элементов вложенных списков list1.
'''
# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for i in list1:
#     # for j in i:
#     #     if j > maximum:
#     #         maximum = j
# # или вот так можно реализовать поиск максимума по элементам всего list1
#     if max(i) > maximum:
#         maximum = max(i)
# print(maximum)
'''
Дополните приведенный код так, чтобы список list1 имел вид:
list1 = [[8, 7, 1], [102, 7, 9], [105, 106, 102], [103, 98, 99, 100], [3, 2, 1]]
'''
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in list1:
#     i.reverse()
# print(list1)
'''
Дополните приведенный код так, чтобы он выводил единственное число: 
сумму всех чисел списка list1 разделённую на общее количество всех чисел.
'''
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for i in list1:
#     total += sum(i)
#     counter += len(i)
# print(total/counter)     


#--------------------------------------------------------------------------------------
'''
Создание вложенных списков
'''
# # Создаёт список длиной n в котором '0' * m элементов

# 1 СПОСОБ!
# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = []
# for _ in range(n):
#     my_list.append([0] * m)
# print(my_list)
# Если ввести значения n = 3, m = 5, то результатом работы такого кода будет:
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# 2 СПОСОБ!
# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [0] * n
# for i in range(n):
#     my_list[i] = [0] * m
# print(my_list)

# 3 СПОСОБ!. - самый лучший
# Можно использовать генератор списка: создадим список из n элементов, 
# каждый из которых будет списком, состоящих из m нулей:
# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [[0] * m for _ in range(n)]
# print(my_list)


#--------------------------------------------------------------------------------------
'''
Считывание вложенных списков
'''
'''
Если элементы списка вводятся через клавиатуру 
(каждая строка на отдельной строке, всего n строк, числа в строке разделяются пробелами), 
для ввода списка можно использовать следующий код:

n = 4 # количество строк (элементов)
my_list = []
for _ in range(n):
    elem = [int(i) for i in input().split()]   # создаем список из элементов строки
    my_list.append(elem)
В этом примере мы используем списочный метод append(), передавая ему в качестве аргумента другой список. Так у нас получается список списков.
В результате, если на вход программе подаются строки
2 4
6 7 8 9
1 3
5 6 5 4 3 1
то в переменной my_list будет храниться список:
[[2, 4], [6, 7, 8, 9], [1, 3], [5, 6, 5, 4, 3, 1]]
'''

#--------------------------------------------------------------------------------------
'''
Перебор и вывод элементов вложенного списка
'''
'''
Когда нужно перебрать все элементы вложенного списка 
(например, чтобы вывести их на экран), обычно используются вложенные циклы.
Рассмотрим программный код:

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=' ')   # используем необязательный параметр end
    print()  

Результатом работы такого кода будет:
1 2 3 
4 5 6 
7 8 9 
'''

'''
Перебор элементов вложенного списка по индексам дает нам больше гибкости для вывода данных. 
Например, поменяв порядок переменных i и j мы получаем иной тип вывода:

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[j][i], end=' ')    # выводим my_list[j][i] вместо my_list[i][j]
    print()

Результатом работы такого кода будет:
1 4 7 
2 5 8 
3 6 9 
'''


#--------------------------------------------------------------------------------------
'''
Обработка вложенных списков
'''
'''
Для обработки элементов вложенного списка, так же как и для вывода его элементов 
на экран как правило используются вложенные циклы.
Используем два вложенных цикла для подсчета суммы всех чисел в списке:

my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
total = 0
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        total += my_list[i][j]
print(total)

Или то же самое с циклом не по индексу, а по значениям:

my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
total = 0
for row in my_list:
    for elem in row:
        total += elem
print(total)

Таким образом можно обработать элементы вложенного списка 
практически в любом языке программирования. 
В Python, однако можно упростить код, если использовать встроенную функцию sum(), 
которая принимает список чисел и возвращает его сумму. 
Подсчет суммы с помощью функции sum() выглядит так:

my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
total = 0
for row in my_list:      # в один цикл
    total += sum(row)
print(total)

Названия переменных row (строка) и elem (элемент) удобно использовать 
при переборе вложенного списка по значениям. 
Названия переменных i и j используются при переборе вложенного списка по индексам.
'''

'''
    Список по образцу 1
На вход программе подается число n. 
Напишите программу, которая создает и выводит построчно список, 
состоящий из n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
    Формат входных данных
На вход программе подается натуральное число nn.
    Формат выходных данных
Программа должна вывести построчно указанный список.
'''
# n = int(input())
# for _ in range(n):
#     my_list = [] 
#     for i in range(1, n+1):
#         my_list.append(i) 
#     print(my_list) 

# n = int(input())
# for _ in range(n):
#     print(list(range(1, n + 1)))

'''
    Список по образцу 2
На вход программе подается число n. 
Напишите программу, которая создает и выводит построчно вложенный список, 
состоящий из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
    Формат входных данных
На вход программе подается натуральное число nn.
    Формат выходных данных
Программа должна вывести построчно указанный вложенный список.
'''
# n = int(input())
# for i in range(1, n+1):
#     my_list = [] 
#     for j in range(1, i+1):
#         my_list.append(j) 
#     print(my_list) 

# n = int(input())
# result = []
# for i in range(1, n + 1):
#     result.append(list(range(1, i + 1)))
# print(*result, sep='\n')

'''
    Треугольник Паскаля 1 🌶️
    Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, 
имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы. 
Каждое число равно сумме двух расположенных над ним чисел.
    На вход программе подается число n. 
Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка 
(нумерация строк начинается с нуля).
    Формат входных данных
На вход программе подается число (n≥0).
    Формат выходных данных
Программа должна вывести указанную строку треугольника Паскаля в виде списка.
Примечание 1. Решение удобно оформить в виде функции pascal(), 
которая принимает номер строки и возвращает соответствующую строку треугольника Паскаля.
'''
# from math import factorial
# n = int(input())
# list1 = []
# for i in range(n+1):
#     a = int(factorial(n) / (factorial(i) * factorial(n-i)))
#     list1.append(a)
# print(list1)

'''
    Треугольник Паскаля 2
На вход программе подается натуральное число n. 
Напишите программу, которая выводит первые n строк треугольника Паскаля.
    Формат входных данных
На вход программе подается число (n≥1).
    Формат выходных данных
Программа должна вывести первые n строк треугольника Паскаля, 
каждую на отдельной строке в соответствии с образцом.
'''
# def pascal(row): # каждый раз строка высчитывается на основе прошлой на каждой итерации 
#     # цикла в основой программе 
#     row = [1] + row
#     for i in range(1, len(row) - 1):
#         row[i] += row[i + 1]
#     return row
# row = []
# n = int(input())
# for _ in range(n):
#     row = pascal(row)
#     print(*row)        

# from math import factorial
# def pascal(n):
#     return [int(factorial(n)/(factorial(i)*factorial(n-i))) for i in range(n+1)]
# n = int(input())
# for j in range(n):
#     print(*pascal(j))

'''
    Упаковка дубликатов 🌶️
На вход программе подается строка текста, содержащая символы. 
Напишите программу, которая упаковывает последовательности одинаковых символов 
заданной строки в подсписки.
    Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
    Формат выходных данных
Программа должна вывести указанный вложенный список.
'''
# s = input().split()
# my_list = [[s[0]]]
# for i in range(0, len(s) - 1):
#     if s[i+1] == s[i]:
#         my_list[-1].append(s[i+1])
#     else:
#         my_list.append([s[i+1]])    
# print(my_list)

'''
    Разбиение на чанки 🌶️
На вход программе подаются две строки, на одной символы, на другой число n. 
Из первой строки формируется список.
Реализуйте функцию chunked(), которая принимает на вход список и число, 
задающее размер чанка (куска), а возвращает список из чанков указанной длины.
    Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные 
символом пробела и число n на отдельной строке.
    Формат выходных данных
Программа должна вывести указанный вложенный список.
Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат 😀.
'''
# s = input().split()
# n = int(input())
# total = []
# for i in range(0, len(s), n):
#     total.append(s[i:i+n])
# print(total)    
      
'''
    Подсписки списка 🌶️🌶️
    Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, 
и даже ни одного. 
Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. 
Список [2, 3] — подсписок списка [1, 2, 3, 4], 
но список [2, 4] не подсписок списка [1, 2, 3, 4], так как элементы 2 и 4 во втором списке 
не смежные. Пустой список — подсписок любого списка. 
Сам список — подсписок самого себя, 
то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].
    На вход программе подается строка текста, содержащая символы. 
Из данной строки формируется список. 
Напишите программу, которая выводит список, 
содержащий все возможные подсписки списка, включая пустой список.
    Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
    Формат выходных данных
Программа должна вывести указанный список, содержащий все возможные подсписки, 
включая пустой список в соответствии с примерами.
    Примечание. Порядок списков одинаковой длины должен соответствовать 
порядку их вхождения в основной список.
'''
# s = input().split()
# total = [[]]
# count = 0
# for i in s:
#     count += 1
#     for j in range(len(s) - count + 1):
#         total.append(s[j:j+count])
# print(total)        