'''
    Факториал
На вход программе подается натуральное число n. 
Напишите программу, которая вычисляет n!.

    Входные данные
На вход программе подается натуральное число n, (n≤12).

    Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.
'''
n = int(input())
total = 1
for i in range(1, n + 1):
    total *= i
print(total)    

# урок пройден