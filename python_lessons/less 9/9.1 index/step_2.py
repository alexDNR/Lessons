'''
    Цифра 1
На вход программе подается одна строка состоящая из цифр. 
Напишите программу, которая считает сумму цифр данной строки.

    Формат входных данных
На вход программе подается одна строка состоящая из цифр.

    Формат выходных данных
Программа должна вывести сумму цифр данной строки.
'''
# n = input()
# summ = 0
# for i in range(len(n)):
#     summ = summ + int(n[i])
# print(summ)    


'''
    Цифра 2
На вход программе подается одна строка. 
Напишите программу, которая выводит сообщение «Цифра» (без кавычек), 
если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).

    Формат входных данных
На вход программе подается одна строка.

    Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''
# s = input()
# count = 0
# for i in range(len(s)):
#     if s[i] in '0123456789':
#         count += 1
# if count > 0:            
#     print("Цифра")
# else:
#     print("Цифр нет")    


'''
    Сколько раз?
На вход программе подается одна строка. 
Напишите программу, которая определяет сколько раз в строке встречаются символы + и *.

    Формат входных данных
На вход программе подается одна строка.

    Формат выходных данных
Программа должна вывести сколько раз встречаются символы  + и * в строке
'''
# s = input()
# count_plus = 0
# count_zvezda = 0
# for i in range(len(s)):
#     if s[i] == "+":
#         count_plus += 1
#     if s[i] == "*":
#         count_zvezda += 1
# print("Символ + встречается", count_plus, "раз")        
# print("Символ * встречается", count_zvezda, "раз")      


'''
    Одинаковые соседи
На вход программе подается одна строка. 
Напишите программу, которая определяет сколько в ней одинаковых соседних символов.

    Формат входных данных
На вход программе подается одна строка.

    Формат выходных данных
Программа должна вывести количество одинаковых соседних символов.
'''
# s = input()
# count = 0
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         count += 1
# print(count)        


'''
    Гласные и согласные
На вход программе подается одна строка с буквами русского языка. 
Напишите программу, которая определяет количество гласных и согласных букв.

    Формат входных данных
На вход программе подается одна строка.

    Формат выходных данных
Программа должна вывести количество гласных и согласных букв.

Примечание. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) 
и 21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).
'''
# s = input().lower()
# glasnie = 0
# soglasnie = 0
# for i in range(len(s)):
#     if s[i] in 'бвгджзйклмнпрстфхцчшщ':
#         soglasnie += 1
#     if s[i] in 'ауоыиэяюёе':
#         glasnie += 1
# print("Количество гласных букв равно", glasnie)
# print("Количество согласных букв равно", soglasnie)          


'''
    Decimal to Binary
На вход программе подается натуральное число, записанное в десятичной системе счисления.
Напишите программу, которая переводит данное число в двоичную систему счисления.

    Формат входных данных
На вход программе подается одно натуральное число.

    Формат выходных данных
Программа должна вывести число записанное в двоичной системе счисления.
'''
# n = int(input())
# code = ''
# while n != 0:
#     code = str(n % 2) + code
#     n //= 2
# print(code)    