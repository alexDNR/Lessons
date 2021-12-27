'''
    Три города
Даны названия трех городов. 
Напишите программу, которая определяет самое короткое и самое длинное название города.

    Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.

    Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

Примечание. Гарантируется, что длины названий всех трех городов различны.
'''
town1 = input()
town2 = input()
town3 = input()
len_town1 = len(town1)
len_town2 = len(town2)
len_town3 = len(town3)
minimum = min(len_town1, len_town2, len_town3)
maximum = max(len_town1, len_town2, len_town3)
if minimum == len_town1:
    print(town1)
elif minimum == len_town2:
    print(town2)
else:
    print(town3)
if maximum == len_town1:
    print(town1)
elif maximum == len_town2:
    print(town2)
else:
    print(town3)

# урок пройден