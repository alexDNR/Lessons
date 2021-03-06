'''
    Угадайка чисел
Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 
и просит пользователя угадать это число. 
Если догадка пользователя больше случайного числа, 
то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'. 
Если догадка меньше случайного числа, то программа должна вывести сообщение 
'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число, 
то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.

Составляющие проекта:
- Целые числа (тип int);
- Переменные;
- Ввод / вывод данных (функции input() и print());
- Условный оператор (if/elif/else);
- Цикл while;
- Бесконечный цикл;
- Операторы break, continue;
- Работа с модулем random для генерации случайных чисел.
'''
# import random

# def number_random():
#     return random.randrange(1, 100)

# rand = number_random()
# while True:
#     n = int(input("Введите число: "))
#     if n < rand:
#         print("Слишком мало, попробуйте еще раз")
#     elif n > rand:
#         print("Слишком много, попробуйте еще раз")
#     else:
#         print("Вы угадали, поздравляем!")    
#         break

'''
    Оптимальная стратегия угадывания числа
Чтобы гарантированно угадать задуманное число от 1 до 100 потребуется не более 7 попыток.
Оптимальный алгоритм угадывания: положим left = 1 и right = 100.
Называем число, равное middle = (left + right) // 2;
Если число middle равно задуманному числу, то мы угадали!;
Если число middle меньше задуманного числа, то положим left = middle + 1 
и продолжим алгоритм;
Если число middle больше задуманного числа, то положим right = middle - 1 
и продолжим алгоритм.
Поскольку на каждой итерации мы отбрасываем половину чисел, то гарантировано 
угадаем задуманное число за величину, равную log_2 n(двоичный логарифм) 
округленную до целого в большую сторону. При n=100 получаем 7 попыток.
'''

'''
    Тимур и его числа
Тимур загадал число от 1 до n. За какое наименьшее количество вопросов 
(на которые Тимур отвечает "больше" или "меньше") 
Руслан может гарантированно угадать число Тимура?
    Формат входных данных
На вход программе подается натуральное число nn.
    Формат выходных данных
Программа должна вывести наименьшее количество вопросов, 
которых гарантированно хватит Руслану, чтобы угадать число Тимура.
'''
# Сама угадайка
# import random
# n = int(input())
# rand = random.randrange(1, n)
# total_question = 1
# left = 1
# right = n
# print("Рандомное число, которое надо угадать:", rand)
# while True:
#     middle = (left + right) // 2
#     print(middle)
#     if middle == rand:
#         #total_question += 1
#         break
#     elif middle < rand:
#         total_question += 1
#         left = middle + 1
#         continue
#     elif middle > rand:
#         total_question += 1
#         right = middle + 1
#         continue
# print('количество:', total_question)    

# опеределение максимального количества попыток угадать число
# from math import *
# n = int(input())
# total_question = ceil(log2(n))
# print(total_question)   

import random
def is_value(n):
    if n.isdigit() and int(n) <= 100:
        return True
    else:
        return False 

print("Добро пожаловать в числовую угадайку")
rand = random.randrange(1, 100) 
count = 0
while True:
    n = input("Введите число от 1 до 100:" )
    if is_value(n):
        n = int(n)
        if n < rand:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            count += 1
            continue
        elif n > rand:
            print("Ваше число больше загаданного, попробуйте еще разок")
            count += 1            
            continue       
        elif n == rand:
            print("Вы угадали, поздравляем!")
            count += 1
            break
    else:
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue

print(f"Спасибо, что играли в числовую угадайку. Количество попыток {count}. \nЕще увидимся...")