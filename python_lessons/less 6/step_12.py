'''
    Интересное число
Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется 
средней по величине цифре. Напишите программу, которая определяет интересное число или нет. 
Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».

    Формат входных данных
На вход программе подается целое трехзначное число.

    Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''
a = int(input())
x1 = a % 10
x2 = (a % 100) // 10
x3 = a // 100
minimum = min(x1, x2, x3)
maximum = max(x1, x2, x3)
avg = (x1 + x2 + x3) - maximum - minimum
if (maximum-minimum) == avg:
    print("Число интересное")
else:
    print("Число неинтересное")    

# урок пройден    