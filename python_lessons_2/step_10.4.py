'''
    Словарь программиста
Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык. 
Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. 
Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из этого словаря.

Формат входных данных
В первой строке задано одно целое число n — количество слов в словаре. В следующих 
n строках записаны слова и их определения, разделенные двоеточием и символом пробела. В следующей строке записано целое число 
m — количество поисковых слов, чье определение нужно вывести. В следующих m строках записаны сами слова, по одному на строке.
    Формат выходных данных
Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести его определение. Если слова в словаре нет, программа должна вывести "Не найдено", без кавычек.
    Примечание 1. Мини-словарь для начинающих разработчиков можно посмотреть тут.
    Примечание 2. Гарантируется, что в определяемом слове или фразе отсутствует двоеточие (:), следом за которым идёт пробел.

Тестовые данные 🟢
Sample Input 1:
5
Змея: язык программирования Python
Баг: от англ. bug — жучок, клоп, ошибка в программе
Конфа: конференция
Костыль: код, который нужен, чтобы исправить несовершенство ранее написанного кода
Бета: бета-версия, приложение на стадии публичного тестирования
3
Змея
Жаба
костыль

Sample Output 1:
язык программирования Python
Не найдено
код, который нужен, чтобы исправить несовершенство ранее написанного кода
'''
# dict1 = {}
# n = int(input())
# for i in range(n):
#     key, value = input().split(': ')
#     dict1[key.lower()] = value
# print(dict1)

# m = int(input())
# words = [input().lower() for i in range(m)]
# print(words)
# for i in words:
#     if i in dict1:
#         print(dict1[i])
#     else:
#         print('Не найдено')    

# Код немного другой - но логика точно такая же
# mydict = {}
# for _ in range(int(input())):
#     key, value = input().split(': ')
#     mydict[key.lower()] = value

# for _ in range(int(input())):
#     print(mydict.get(input().lower(), 'Не найдено'))

'''
    Анаграммы 1
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). 
Например, английские слова evil и live – это анаграммы.
    На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.
    Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.
    Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.

Тестовые данные 🟢
Sample Input 1:
thing
night

Sample Output 1:
YES

Sample Input 2:
cat
rat

Sample Output 2:
NO
'''
# word1 = input()
# word2 = input()
# print('YES' if sorted(word1) == sorted(word2) else 'NO')

'''
    Анаграммы 2
На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет. 
Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.
    Формат входных данных
На вход программе подаются два предложения, каждое на отдельной строке.
    Формат выходных данных
Программа должна вывести YES , если предложения – анаграммы и NO в противном случае.
    Примечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-. Других символов в тексте нет.

Тестовые данные 🟢
Sample Input 1:
Вижу зверей
Живу резвей

Sample Output 1:
YES

Sample Input 2:
Когда увидимся
тогда и свидимся

Sample Output 2:
NO
'''
