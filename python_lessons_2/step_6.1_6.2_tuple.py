'''
    Функция tuple()
Встроенная функция list() может применяться для преобразования кортежа в список.
    Приведенный ниже код:
number_tuple = (1, 2, 3, 4, 5)
number_list = list(number_tuple)
print(number_list)
    выводит:
[1, 2, 3, 4, 5]

и наоборот

Встроенная функция tuple()  может применяться для преобразования списка в кортеж.
    Приведенный ниже код:
str_list = ['один', 'два', 'три']
str_tuple = tuple(str_list)
print(str_tuple)
    выводит:
('один', 'два', 'три')

Аналогичным образом мы можем создать кортеж на основании строки.
    Приведенный ниже код:
text = 'hello python'
str_tuple = tuple(text)
print(str_tuple)
    выводит:
('h', 'e', 'l', 'l', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n') 
- в кортеже содержится и проблел после преобразования из строки

Преобразование строки в список позволяет получить список символов строки. 
Это может быть полезно, например, когда надо изменить один символ строки.
    Приведенный ниже код:
s = 'симпотичный'
print(s)
a = list(s)
a[4] = 'а'
s = ''.join(a)
print(s)
    Приведенный выше код выводит:
симпотичный
симпатичный
'''

'''
    Особенности кортежей
Кортежи поддерживают те же операции, что и списки, 
за исключением изменяющих содержимое.
    Кортежи поддерживают:
- доступ к элементу по индексу (только для получения значений элементов);
- методы, в частности index(), count();
- встроенные функции, в частности len(), sum(), min() и max();
- срезы;
- оператор принадлежности in;
- операторы конкатенации (+) и повторения (*).
'''

# ЗАДАЧИ
'''
Дополните приведенный код, используя срезы, 
так чтобы он вывел первые 6 элементов кортежа primes.
Примечание. Результатом вывода должна быть строка (2, 3, 5, 7, 11, 13).
'''
# primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71) 
# print(primes[:6])

'''
Дополните приведенный код, используя срезы, 
так чтобы он вывел элементы кортежа countries, кроме первых двух.
Примечание. Результатом вывода должна быть строка 
('Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 
'Ukraine', 'Chile', 'Cameroon').
'''
# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 
# 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[2:])

'''
Дополните приведенный код, используя срезы, чтобы он вывел все элементы 
кортежа countries, кроме последних трех.
Подсказка
Не забывайте, что элементы кортежа нумеруются с -1 начиная с конца.
'''
# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 
# 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[:-3])

'''
Дополните приведенный код, используя срезы, 
чтобы он вывел все элементы кортежа countries, 
кроме двух последних и трех первых.
'''
# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 
# 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[3:-2])

'''
Дополните приведенный код так, чтобы переменная number содержала количество 
элементов кортежа countries.
    Подсказка
Используйте встроенную функцию len().
'''
# countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 
# 'Slovakia', 'Slovenia', 'Hungary')
# number = len(countries)
# print(number)

'''
Дополните приведенный код так, чтобы он вывел сумму минимального 
и максимального элементов кортежа numbers.
'''
# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
# print(min(numbers) + max(numbers))

'''
Дополните приведенный код так, чтобы переменная index, 
содержала индекс элемента «Slovenia» в кортеже countries.
'''
# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 
# 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)

'''
Дополните приведенный код так, чтобы переменная number, 
содержала количество вхождений «Spain» в кортеж countries.
'''
# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 
# 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
# number = countries.count('Spain')
# print(number)

'''
Дополните приведенный код, используя операторы конкатенации (+) 
и умножения кортежа на число (*), чтобы он вывел кортеж:
(1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13).
'''
# numbers1 = (1, 2, 3)
# numbers2 = (6,)
# numbers3 = (7, 8, 9, 10, 11, 12, 13)
# print(numbers1*2 + numbers2*9 + numbers3)

'''
В переменную city_name вводится название города (например, Москва), 
а в переменную city_year – год его основания (например, 1147). 
Заполните пропущенную строку таким образом, 
чтобы в переменной city оказался кортеж из значений этих двух переменных 
(сначала название города, затем год основания).
'''
# city_name = input()
# city_year = int(input())
# city = (city_name, city_year)
# print(city)

'''
Дополните приведенный код, так чтобы получить список, 
содержащий только непустые кортежи исходного списка tuples, 
не меняя порядка их следования.
    Подсказка 1
Для проверки пустоты кортежа используйте встроенную функцию len().
    Подсказка 2
Используйте списочное выражение.
'''
# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# non_empty_tuples = [i for i in tuples if len(i) != 0]
# print(non_empty_tuples)

'''
Дополните приведенный код так, чтобы переменная new_tuples, 
содержала список кортежей на основе списка tuples 
с последним элементом каждого кортежа, замененным на численное значение 100.
    Подсказка 1
Используйте списочное выражение.
    Подсказка 2
Чтобы получить все элементы кортежа t кроме последнего, используем срез t[:-1].
    Подсказка 3
Чтобы создать кортеж, содержащий единственный элемент 100, мы используем (100,).
'''
# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), 
# (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = [i[:-1]+(100,) for i in tuples]
# print(new_tuples)