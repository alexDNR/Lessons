'''
    Ревью кода-2 🌶️🌶️
На обработку поступает последовательность из 10 целых чисел. 
Известно, что вводимые числа по абсолютной величине не превышают 10^6. 
Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел 
последовательности и максимальное отрицательное число в последовательности. 
Если отрицательных чисел нет, требуется вывести на экран «NO». 
Программист торопился и написал программу неправильно.

Найдите все ошибки в этой программе (их ровно 5). 
Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена 
без изменения других строк.
'''
mx = -1000000000000
s = 0
for i in range(1, 10+1):
    x = int(input())
    if x < 0:
        s += x
    if (x > mx) and (x < 0):
        mx = x
if s >= 0:
    print("NO")
else:             
    print(s)
    print(mx)
    