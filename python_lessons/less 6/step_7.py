'''
    Dog age
На вход программе подается число n – количество собачьих лет. 
Напишите программу, которая вычисляет возраст собаки в человеческих годах.

    Формат входных данных
На вход программе подаётся натуральное число – количество собачьих лет.

    Формат выходных данных
Программа должна вывести возраст собаки в человеческих годах.

Примечание. В течение первых двух лет собачий год равен 10.5 человеческим годам. 
После этого каждый год собаки равен 4 человеческим годам.
'''
age = int(input())
if age <= 2:
    age_1 = age * 10.5
    print(age_1)
else:
    age_x = age - 2
    age_2 = age_x * 4 + 21
    print(age_2)    

# урок пройден    