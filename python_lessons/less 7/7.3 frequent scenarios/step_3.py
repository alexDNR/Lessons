'''
    Асимптотическое приближение
На вход программе подается натуральное число n. 
Напишите программу, которая вычисляет значение выражения
(1 + 1/2 + 1/3 + ... + 1/n) - ln(n)

Примечание. Для вычисления натурального логарифма 
воспользуйтесь функцией log(n), которая находится в модуле math.
'''
from math import *
n = int(input())
summ = 0
for i in range(1, n+1):
    summ += 1/i   
answer = summ - log(n)   
print(answer)

# урок пройден