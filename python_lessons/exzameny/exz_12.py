# numbers = list(range(1, 10, 2))
# for i in numbers:
#     print(i, end='*')

# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[1:3]
# print(my_list)

'''
    Список четных
На вход программе подается четное число n, n≥2. 
Напишите программу, которая выводит список четных чисел
[2, 4, 6, ..., n].
    Формат входных данных
На вход программе подается четное натуральное число.
    Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''
# numbers = [i for i in range(1, int(input())+1) if i%2==0]
# print(numbers)

'''
    Сумма двух списков
На вход программе подаются две строки текста, 
содержащие целые числа. Из данных строк формируются списки чисел 
L и M. Напишите программу, которая создает третий список, 
элементами которого являются суммы соответствующих элементов 
списков L и M. Далее программа должна вывести каждый элемент 
полученного списка на одной строке через 1 пробел.
    Формат входных данных
На вход программе подаются две строки текста, 
содержащие целые числа, разделенные символом пробела.
    Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Количество чисел в обеих строках одинаковое.
'''
# a = input().split()
# b = input().split()
# answer = []
# for i in range(len(a)):
#     answer.append(int(a[i])+int(b[i]))
# print(*answer)    

'''
    Сумма чисел
На вход программе подается строка текста, 
содержащая натуральные числа. 
Напишите программу, которая вставляет между каждым числом знак +, 
а затем вычисляет сумму полученных чисел.
    Формат входных данных
На вход программе подается строка текста, 
содержащая натуральные числа, разделенные символом пробела.
    Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Строковый метод join() работает только со списком строк.
'''
# s = input().split()
# total = 0
# for i in range(len(s)):
#     total += int(s[i])
# print(*s, sep='+', end='')    
# print('=', total, sep='')


'''
    Валидный номер 🌶️🌶️
На вход программе подается строка текста. 
Напишите программу, которая определяет является ли введенная строка корректным 
телефонным номером. Строка текста является корректным телефонным номером 
если она имеет формат:
    abc-def-hijk или
    7-abc-def-hijk
где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
    Формат входных данных 
На вход программе подается строка текста.
    Формат выходных данных
Программа должна вывести «YES» если строка является корректным телефонным номером 
и «NO» в противном случае.
Примечание. Телефонный номер должен содержать только цифры и символ -, 
а количество цифр в каждой группе должны быть правильным.
'''
# phone = input()
# if '-' in phone:
#     phone = phone.split('-')
#     phone2 = ''.join(phone)
#     if phone2.isdigit():
#         if len(phone) == 4:
#             if len(phone[0]) == 1 and phone[0] == '7':
#                 if len(phone[1]) == 3 and len(phone[2]) == 3 and len(phone[3]) == 4:
#                     print("YES")
#                 else:
#                     print("NO")
#             else:
#                 print("NO")        
#         elif len(phone) == 3: 
#             if len(phone[0]) == 3 and len(phone[1]) == 3 and len(phone[2]) == 4:
#                 print("YES")
#             else:
#                 print("NO")                    
#     else:
#         print("NO")                    
# else:
#     print("NO")

'''
    Самый длинный
На вход программе подается строка текста. 
Напишите программу, использующую списочное выражение, 
которая находит длину самого длинного слова.
    Формат входных данных
На вход программе подается строка текста.
    Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''
# s = input().split()
# total = 0
# for i in s:
#     t = len(i)
#     if t > total:
#         total = t
# print(total)    

# s = [len(i) for i in input().split()]
# print(max(s))

'''
    Молодежный жаргон
На вход программе подается строка текста. 
Напишите программу, использующую списочное выражение, 
которая преобразует каждое слово введенного текста в "молодежный жаргон" 
по следующему правилу: 
- первая буква каждого слова удаляется и ставится в конец слова; 
- затем в конец слова добавляется слог "ки".
    Формат входных данных
На вход программе подается строка текста на русском языке.
    Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''
# s = [i[1:]+i[0]+'ки' for i in input().split()]
# print(*s)
