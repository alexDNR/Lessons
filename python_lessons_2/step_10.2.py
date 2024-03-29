# my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
# print(min(my_dict) + max(my_dict))

'''
Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), чей номер оканчивается на 
8
'''
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

# users_name = []
# for i in users:
#     if i['phone'][-1] == '8':
#         users_name.append(i['name'])
# print(*sorted(users_name))               

'''
Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), 
у которых нет информации об электронной почте. 
    Примечание 1. Ключ email может отсутствовать в словаре.
    Примечание 2. Имена необходимо вывести на одной строке, разделяя символом пробела.
'''
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# users_name = []
# for i in users:
#     if 'email' not in i or i['email'] == '':
#         users_name.append(i['name'])
# print(*sorted(users_name)) 

'''
Строковое представление
Напишите программу, которая будет превращать натуральное число в строку, 
заменяя все цифры в числе на слова:
0 на zero;
1 на one;
2 на two;
3 на three;
4 на four;
5 на five;
6 на six;
7 на seven;
8 на eight;
9 на nine.
    Формат входных данных
На вход программе подается натуральное число.
    Формат выходных данных
Программа должна вывести строковое представление числа.
Примечание. Используйте словарь вместо условного оператора.
    Тестовые данные 🟢
Sample Input 1:
230
    Sample Output 1:
two three zero
'''
# d = {
#     '0': "zero",
#     '1': "one",
#     '2': "two",
#     '3': "three",
#     '4': "four",
#     '5': "five",
#     '6': "six",
#     '7': "seven",
#     '8': "eight",
#     '9': "nine"
# }
# s = input()
# for i in s:
#     print(d[i], end=' ')

'''
Информация об учебных курсах
Напишите программу, которая по номеру курса выводит информацию о данном курсе. 
Номер курса (ключ)	Номер аудитории (значение)	Преподаватель (значение)	Время (значение)
CS101	3004	Хайнс	8:00
CS102	4501	Альварадо	9:00
CS103	6755	Рич	10:00
NT110	1244	Берк	11:00
CM241	1411	Ли	13:00
    Формат входных данных
На вход программе подается одна строка – номер курса.
    Формат выходных данных
Программа должна вывести номер курса, затем номер аудитории, имя преподавателя и время проведения курса в соответствии с примерами.
    Примечание 1. Используйте словарь вместо условного оператора.
    Примечание 2. Для удобного вывода используйте строковый метод format() или f-строки.
    Тестовые данные 🟢
Sample Input 1:
CS101

Sample Output 1:   
CS101: 3004, Хайнс, 8:00
'''
# course = {
#     'CS101': '3004, Хайнс, 8:00',
#     'CS102': '4501, Альварадо, 9:00',
#     'CS103': '6755, Рич, 10:00',
#     'NT110': '1244, Берк, 11:00',
#     'CM241': '1411, Ли, 13:00',
# }
# course_number = input()
# print(f"{course_number}: {course[course_number]}")

'''
    Набор сообщений
На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры. 
Поскольку с каждой клавишей связано несколько букв, для большинства букв требуется несколько нажатий клавиш. 
При однократном нажатии цифры генерируется первый символ, указанный для этой клавиши. 
1	.,?!:
2	ABC
3	DEF
4	GHI
5	JKL
6	MNO
7	PQRS
8	TUV
9	WXYZ
0	space (пробел)
    Напишите программу, которая отображает нажатия клавиш, необходимые для введенного сообщения.
    Формат входных данных
На вход программе подается одна строка – текстовое сообщение.
    Формат выходных данных
Программа должна вывести нажатия клавиш, необходимых для введенного сообщения.
Примечание 1. Ваша программа должна обрабатывать как прописные, так и строчные буквы.
Примечание 2. Ваша программа должна игнорировать любые символы, не указанные в приведенной выше таблице.
'''
# d = {
#     ".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111',
#     "a": '2', "b": '22', "c": '222',
#     "d": '3', "e": '33', "f": '333',
#     "g": '4', "h": '44', "i": '444',
#     "j": '5', "k": '55', "l": '555',
#     "m": '6', "n": '66', "o": '666',
#     "p": '7', "q": '77', "r": '777', "s": '7777',
#     "t": '8', "u": '88', "v": '888',
#     "w": '9', "x": '99', "y": '999', "z": '9999',
#     " ": '0'
# }
# s = input().lower().replace('"', '')
# for i in s:
#     print(d[i], end='')

'''
    Код Морзе
Код Морзе для представления цифр и букв использует тире и точки.
Напишите программу для кодирования текстового сообщения в соответствии с кодом Морзе.
Символ	Код	Символ	Код	Символ	Код	Символ	Код
A	.-	J	.---	S	...	1	.----
B	-...	K	-.-	T	-	2	..---
C	-.-.	L	.-..	U	..-	3	...--
D	-..	M	--	V	...-	4	....-
E	.	N	-.	W	.--	5	.....
F	..-.	O	---	X	-..-	6	-....
G	--.	P	.--.	Y	-.--	7	--...
H	....	Q	--.-	Z	--..	8	---..
I	..	R	.-.	0	-----	9	----.
    Формат входных данных
На вход программе подается одна строка – текстовое сообщение.
Формат выходных данных
Программа должна вывести закодированное с помощью кода Морзе сообщение, оставляя пробел между каждым закодированным символом (последовательностью тире и точек).
Примечание 1. Ваша программа должна игнорировать любые символы, не перечисленные в таблице.
    Тестовые данные 🟢
Sample Input 1:
Interstellar

Sample Output 1:
.. -. - . .-. ... - . .-.. .-.. .- .-.
'''
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = [
#     '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', 
#     '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', 
#     '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', 
#     '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.'
#     ]
# morse_code = dict(zip(letters, morse))    
# s = input().upper()
# for i in s:
#     if not i in "' ',.+=?!-":
#         print(morse_code[i], end=' ')