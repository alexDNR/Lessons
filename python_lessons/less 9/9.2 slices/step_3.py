'''
    Делаем срезы 1
На вход программе подается одна строка. Напишите программу, которая выводит:
- общее количество символов в строке;
- исходную строку повторенную 3 раза;
- первый символ строки;
- первые три символа строки;
- последние три символа строки;
- строку в обратном порядке;
- строку с удаленным первым и последним символом.
    Формат входных данных
На вход программе подается одна строка, длина которой больше 3 символов.
    Формат выходных данных
Программа должна вывести данные в соответствии с условием. 
Каждое значение выводится на отдельной строке.
'''
# s = input()
# print(len(s))
# print(s*3)
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:-1])


'''
    Делаем срезы 2
На вход программе подается одна строка. 
Напишите программу, которая выводит:
- третий символ этой строки;
- предпоследний символ этой строки;
- первые пять символов этой строки;
- всю строку, кроме последних двух символов;
- все символы с четными индексами;
- все символы с нечетными индексами;
- все символы в обратном порядке;
- все символы строки через один в обратном порядке, начиная с последнего.
    Формат входных данных
На вход программе подается одна строка, длина которой больше 5 символов.
    Формат выходных данных
Программа должна вывести данные в соответствии с условием. 
Каждое значение выводится на отдельной строке.
'''
# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-1][::2])


'''
    Две половинки
На вход программе подается строка текста. 
Напишите программу, которая разрежет ее на две равные части, 
переставит их местами и выведет на экран.
    Формат входных данных
На вход программе подается строка текста.
    Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Если длина строки нечетная, 
то длина первой части должна быть на один символ больше.
'''
# s = input()
# if len(s) % 2 == 0:
#     print(s[int(len(s)/2):] + s[:int(len(s)/2)])
# else:
#     print(s[int(len(s)/2)+1:] + s[:int(len(s)/2)+1])
