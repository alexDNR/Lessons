'''
    Ведьмаку заплатите чеканной монетой
Всем известно, что ведьмак способен одолеть любых чудовищ, 
однако его услуги обойдутся недешево, к тому же ведьмак не принимает купюры, 
он принимает только чеканные монеты. 
В мире ведьмака существуют монеты с номиналами 1,5,10,25.

Напишите программу, которая определяет какое минимальное количество чеканных монет 
нужно заплатить ведьмаку.

    Формат входных данных 
На вход программе подается одно натуральное число, цена за услугу ведьмака.

    Формат выходных данных
Программа должна вывести минимально возможное количество чеканных монет для оплаты.
'''
n = int(input())
count = 0
while n >= 25:
    count += 1
    n -= 25
while n >= 10:
    count += 1
    n -= 10
while n >= 5:
    count += 1
    n -= 5       
while n >= 1:
    count += 1
    n -= 1
print(count)         

# урок пройден