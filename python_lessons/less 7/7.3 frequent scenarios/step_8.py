'''
    Знакочередующаяся сумма
На вход программе подается натуральное число n. 
Напишите программу вычисления знакочередующей суммы 1-2+3-4+5-6 + ... + (-1)^{n+1}n.

    Входные данные
На вход программе подается натуральное число n.

    Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.
'''
n = int(input())
summ = 0
for i in range (1, n+1):
    if i % 2 == 0:
        i = -i
    summ += i
print(summ)    

# урок пройден