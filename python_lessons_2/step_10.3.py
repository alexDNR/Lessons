# result = {}
# for num in range(1,16):
#     result[num] = result.get(num, num**2)

# print(result)    


'''
Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам, 
складывая значения по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях. 
Результирующий словарь необходимо присвоить переменной result.

Примечание. Выводить содержимое словаря result не нужно.
'''
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'z': 666, 'b': 200, 'c': 12, 'd': 400, 't': 777,  'p': 123, 'w': 111, }

# result = {}
# result = dict2
# for i in dict1:
#     if i in dict2:
#         result[i] = dict1[i] + dict2[i]
#     else:
#         result[i] = dict1[i]    
     
# print(result)


'''
Дополните приведенный код так, чтобы в переменной result хранился словарь, 
в котором для каждого символа строки text будет подсчитано количество его вхождений.

Примечание. Выводить содержимое словаря result не нужно.
'''
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

# result = {}
# for i in text:
#     result[i] = result.get(i, text.count(i))

# print(result)    


'''
Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. 
Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.
'''
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# list_s = s.split()
# result = {}
# for i in list_s:
#     result[i] = result.get(i, list_s.count(i))

# for i in sorted(result.items()):
#     if i[1] == max(result.values()):
#         print(i[0])
#         break


#Пихаю в словарь пары кол-во повторений : слово из отсортированного наоборот списка, 
#чтобы последним наибольшим ключом было слово, которое меньше в лексикографическом порядке. 

#dict1 = {s.count(i): i for i in sorted(s.split(), reverse=True)}
# print(dict1[max(dict1)])


'''
Вам доступен список pets, содержащий информацию о собаках и их владельцах.  
Каждый элемент списка – это кортеж вида (кличка собаки, имя владельца, фамилия владельца, возраст владельца).

Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут перечислены его собаки. 
Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список кличек собак (сохранив исходный порядок следования).
    Примечание 1. Не забывайте: кортежи являются неизменяемыми, поэтому могут быть ключами словаря.
    Примечание 2. Обратите внимание, что у некоторых владельцев по несколько собак.
    Примечание 3. Выводить содержимое словаря result не нужно.
'''
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]

# result = {}
# for i in pets:
#     result.setdefault((i[1], i[2], i[3]), []).append(i[0])
# print(result)    
'''
Метод setdefault() позволяет получить значение из словаря по заданному ключу, автоматически добавляя элемент словаря, если он отсутствует.
Метод принимает два аргумента:
key: ключ, значение по которому следует получить, если таковое имеется в словаре, либо создать.
default: значение, которое будет использовано при добавлении нового элемента в словарь.
В зависимости от значений параметров key и default возможны следующие сценарии работы данного метода.
'''


'''
Самое редкое слово 🌶️
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. 
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
    Формат входных данных
На вход программе подается строка текста.
    Формат выходных данных
Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.
Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.
Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать 
пробелы и знаки препинания .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.
    Sample Input 1:
home sweet home

    Sample Output 1:
sweet

    Sample Input 2:
home sweet home sweet.

    Sample Output 2:
home
'''
# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
# result = {}
# for i in lst:
#     result[i] = result.get(i, lst.count(i)) # создаём словарь где ключ это слово из строки, а значение это количество повторений этого слова

# for i in sorted(result.items()): # прогоняем отсортированный кортеж ключ-значение из словаря
#     if i[1] == min(result.values()): # ищем минимальное значение "значения" словаря 
#         print(i[0]) # печатаем ключ этого значения
#         break 

# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
# dict1 = {lst.count(i): i for i in sorted(lst, reverse=True)}
# print(dict1[min(dict1)])


'''
Исправление дубликатов 🌶️
На вход программе подается строка, содержащая строки-идентификаторы. 
Напишите программу, которая исправляет их так, чтобы в результирующей строке не было дубликатов. 
Для этого необходимо прибавлять к повторяющимся идентификаторам постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.
    Формат входных данных
На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.
    Формат выходных данных
Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.
    Тестовые данные 🟢
Sample Input 1:
a b c a a d c

Sample Output 1:
a b c a_1 a_2 d c_1
'''
# s = input().split()
# result = {}
# for i in s:
#     result[i] = result.get(i, 0)+1 # ведём подсчёт повторения значения
#     # print(result[i]) # вот эта строка выводит значения по ключу i
#     if result[i] == 1: # если первый раз появился символ - то счётчик будет = 1
#         print(f"{i}", end=' ') # если да, то просто выводим сам символ и всё
#     else:
#         print(f"{i}_{result[i]-1}", end=' ') # если он уже попадался, то счётчик у него будет +1, поэтому выводим -1