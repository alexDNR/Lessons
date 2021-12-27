'''
Метод insert()
Метод index()
Метод remove()
Метод pop()
Метод reverse()
Метод count()
Метод clear()
Метод copy()
Метод sort()
'''

'''
Метод insert() позволяет вставлять значение в список в заданной позиции. 
В него передается два аргумента:
- index: индекс, задающий место вставки значения;
- value: значение, которое требуется вставить.

Следующий программный код:
names = ['Gvido', 'Roman' , 'Timur']
print(names)
names.insert(0, 'Anders')
print(names)
names.insert(3, 'Josef')
print(names)

выведет:
['Gvido', 'Roman' , 'Timur']
['Anders', 'Gvido', 'Roman' , 'Timur']
['Anders', 'Gvido', 'Roman' , 'Josef', 'Timur']
'''

'''
Метод index() возвращает индекс первого элемента, 
значение которого равняется переданному в метод значению. 
Таким образом, в метод передается один параметр:
- value: значение, индекс которого требуется найти.
Если элемент в списке не найден, то во время выполнения происходит ошибка.

Следующий программный код:
names = ['Gvido', 'Roman' , 'Timur']
position = names.index('Timur')
print(position)

выведет:
2
'''

'''
Метод remove() удаляет первый элемент, значение которого равняется переданному 
в метод значению. В метод передается один параметр:
- value: значение, которое требуется удалить.
Метод уменьшает размер списка на один элемент. 
Все элементы после удаленного элемента смещаются на одну позицию к началу списка. 
Если элемент в списке не найден, то во время выполнения происходит ошибка.

Следующий программный код:
food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
print(food)
food.remove('Рис')
print(food)

выведет:
['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
['Курица', 'Рыба', 'Брокколи', 'Рис']

Важно: метод remove() удаляет только первый элемент с указанным значением. 
Все последующие его вхождения остаются в списке. 
Чтобы удалить все вхождения нужно использовать цикл while 
в связке с оператором принадлежности in и методом remove.
'''

'''
Метод pop() удаляет элемент по указанному индексу и возвращает его. 
В метод pop() передается один необязательный аргумент:
- index: индекс элемента, который требуется удалить.
Если индекс не указан, то метод удаляет и возвращает последний элемент списка. 
Если список пуст или указан индекс за пределами диапазона, 
то во время выполнения происходит ошибка.

Следующий программный код:
names = ['Gvido', 'Roman' , 'Timur']
item = names.pop(1)
print(item)
print(names)

выведет:
Roman
['Gvido', 'Timur']
'''

'''
Метод count() возвращает количество элементов в списке, 
значения которых равны переданному в метод значению. 
Таким образом, в метод передается один параметр:
- value: значение, количество элементов, равных которому,  нужно посчитать.
Если значение в списке не найдено, то метод возвращает 0.

Следующий программный код:
names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
cnt1 = names.count('Timur')
cnt2 = names.count('Gvido')
cnt3 = names.count('Josef')
print(cnt1)
print(cnt2)
print(cnt3)

выведет:
3
1
0
'''

'''
Метод reverse() инвертирует порядок следования значений в списке, 
то есть меняет его на противоположный.

Следующий программный код:
names = ['Gvido', 'Roman' , 'Timur']
names.reverse()
print(names)

выведет:
['Timur', 'Roman', 'Gvido']
Существует большая разница между вызовом метода names.reverse() 
и использованием среза names[::-1]. 
Метод reverse() меняет порядок элементов на обратный в текущем списке, 
а срез создает копию списка, в котором элементы следуют в обратном порядке.
'''

'''
Метод clear() удаляет все элементы из списка.

Следующий программный код:
names = ['Gvido', 'Roman' , 'Timur']
names.clear()
print(names)

выведет:
[]
'''

'''
Метод copy() создает поверхностную копию списка.

Следующий программный код:
names = ['Gvido', 'Roman' , 'Timur']
names_copy = names.copy()              # создаем поверхностную копию списка names
print(names)
print(names_copy)

выведет:
['Gvido', 'Roman', 'Timur']
['Gvido', 'Roman', 'Timur']
Аналогичного результата можно достичь с помощью срезов или функции list():

names = ['Gvido', 'Roman' , 'Timur']
names_copy1 = list(names)             # создаем поверхностную копию с помощью функции list()
names_copy2 = names[:]                # создаем поверхностную копию с помощью среза от начала до конца
'''


'''
    Все сразу 2 🌶️
Дополните приведенный код, чтобы он:
- Заменил второй элемент списка на 17;
- Добавил числа 4, 5 и 6 в конец списка;
- Удалил первый элемент списка;
- Удвоил список;
- Вставил число 25 по индексу 3;
- Вывел список, с помощью функции print()
'''
# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4,5,6])
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)


'''
    Переставить min и max
На вход программе подается строка текста, содержащая различные натуральные числа. 
Из данной строки формируется список чисел. 
Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
    Формат входных данных
На вход программе подается строка текста, содержащая различные натуральные числа, 
разделенные символом пробела.
    Формат выходных данных
Программа должна вывести строку текста в соответствии с условием задачи.
Примечание. Используйте подходящие встроенные функции и списочные методы.
'''
# s = input().split()
# s = [int(i) for i in s]
# maxim = max(s)
# index_max = s.index(maxim)
# minim = min(s)
# index_min = s.index(minim)
# s[index_max], s[index_min] = s[index_min], s[index_max]
# print(*s)


'''
    Количество артиклей
На вход программе подается строка, содержащая английский текст. 
Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.
    Формат входных данных
На вход программе подается строка, содержащая английский текст. 
Слова текста разделены символом пробела.
    Формат выходных данных
Программа должна вывести общее количество артиклей 'a', 'an', 'the' 
вместе с поясняющим текстом.
Примечание. Артикли могут начинаться с заглавной буквы 'A', 'An', 'The'.
'''
# text = input().lower().split()
# art_a = text.count('a')
# art_an = text.count('an')
# art_the = text.count('the')
# print("Общее количество артиклей:", art_a+art_an+art_the)


'''
    Взлом Братства Стали 🌶️
Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – 
секретный бункер Братства Стали, и любезно соглашается помочь им в решении их проблем. 
Одной из такой проблем являлся странный компьютерный вирус, 
который проявлялся в виде появления комментариев к программам на терминалах Братства Стали. 
Известно, что программисты Братства никогда не оставляют комментарии к коду, 
и пишут программы на Python, поэтому удаление всех этих комментариев никак не навредит им. 
Помогите писцу Ибсену удалить все комментарии из программы.
    Формат входных данных
На первой строке вводится символ решётки и сразу же натуральное число n — 
количество строк в программе, не считая первой. Далее следует n строк кода.
    Формат выходных данных
Нужно вывести те же строки, но удалить комментарии и символы пустого пространства 
в конце строк. Пустую строку вместо первой строки ввода выводить не надо.
'''
# n = input()
# text = []
# for _ in range(int(n[1:])):
#     s = input()
#     if "#" in s:
#         s = s[:s.find('#')]
#         text.append(s.rstrip())
#     else:
#         text.append(s.rstrip())    
# print(*text, sep='\n')    


'''
Метод sort(), который сортирует элементы списка по возрастанию или убыванию.

Следующий программный код:
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
a.sort()
print('Отсортированный список:', a)

выведет:
Отсортированный список: [-67, -3, -2, 0, 1, 6, 7, 8, 9, 12, 34, 45, 99, 1000]
-----------------------------------------------------------------------------
По умолчанию метод sort() сортирует список по возрастанию. 
Если требуется отсортировать список по убыванию, 
необходимо явно указать параметр reverse = True.

Следующий программный код:
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
a.sort(reverse = True)   # сортируем по убыванию
print('Отсортированный список:', a)

выведет:
Отсортированный список: [1000, 99, 45, 34, 12, 9, 8, 7, 6, 1, 0, -2, -3, -67]
-----------------------------------------------------------------------------
С помощью метода sort() можно сортировать списки содержащие не только числа, но и строки. 
В таком случае элементы списка сортируются в соответствии с лексикографическим порядком.

Следующий программный код:
a = ['бета', 'альфа', 'дельта', 'гамма']
a.sort()
print ('Отсортированный список:', a)

выведет:
Отсортированный список: ['альфа', 'бета', 'гамма', 'дельта']

Примечание 2. Метод sort() использует алгоритм Timsort.
'''

'''
    Сортировка чисел
На вход программе подается строка текста, содержащая целые числа. 
Из данной строки формируется список чисел. 
Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, 
а затем по убыванию. 
    Формат входных данных
На вход программе подается строка текста, содержащая целые числа, 
разделенные символом пробела.
    Формат выходных данных
Программа должна вывести две строки текста в соответствии с условием задачи.
'''
# n = [int(i) for i in input().split()]
# n.sort()
# print(*n)
# n.sort(reverse=True)
# print(*n)
