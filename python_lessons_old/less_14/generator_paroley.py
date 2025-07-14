'''
    Генератор безопасных паролей
Описание проекта: программа генерирует заданное количество паролей и включает 
в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, 
а какие исключить.
Составляющие проекта:
- Целые числа (тип int);
- Переменные;
- Ввод / вывод данных (функции input() и print());
- Условный оператор (if/elif/else);
- Цикл for;
- Написание пользовательских функций;
- Работа с модулем random для генерации случайных чисел.
'''

'''
Программа должна запрашивать у пользователя следующую информацию:
Количество паролей для генерации;
Длину одного пароля;
Включать ли цифры 0123456789?
Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
Включать ли символы !#$%&*+-=?@^_?
'''

import random
from termcolor import colored, cprint

digits =  '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def add_digit(): # функция для добавления цифр в пароль
    while True:
        print(colored("Включать ли цифры 0123456789? (да/нет)", 'green', attrs=['underline']))
        queshion = input().lower().strip()
        if queshion == 'да' or queshion == 'нет':        
            if queshion == 'да':
                return True
                break
            elif queshion == 'нет':
                return False
                break
        else:
            print("введите верное значение для ответа на вопрос")
            continue

def add_lower_ch(): # функция для добавления прописных букв в пароль
    while True:
        print(colored("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет)", 'green', attrs=['underline']))
        queshion = input().lower().strip()
        if queshion == 'да' or queshion == 'нет':        
            if queshion == 'да':
                return True
                break
            elif queshion == 'нет':
                return False
                break
        else:
            print("введите верное значение для ответа на вопрос")
            continue

def add_upper_ch(): # функция для добавления загравных букв в пароль
    while True:
        print(colored("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет)", 'green', attrs=['underline']))
        queshion = input().lower().strip()      
        if queshion == 'да' or queshion == 'нет':        
            if queshion == 'да':
                return True
                break
            elif queshion == 'нет':
                return False
                break
        else:
            print("введите верное значение для ответа на вопрос")
            continue

def add_special_ch(): # функция для добавления спец. символов в пароль
    while True:
        print(colored("Включать ли символы !#$%&*+-=?@^_? (да/нет)", 'green', attrs=['underline']))
        queshion = input().lower().strip()        
        if queshion == 'да' or queshion == 'нет':        
            if queshion == 'да':
                return True
                break
            elif queshion == 'нет':
                return False
                break
        else:
            print("введите верное значение для ответа на вопрос")
            continue

def len_pass(): # функция для опеределения длины пароля
    while True:
        print(colored("Введите количество символов для пароля (до 20 символов):" , 'blue', attrs=['underline']))
        len_pass = int(input())
        if len_pass <= 20 and len_pass != 0 and len_pass > 0:
            return len_pass
            print("Введёна корретная длина пароля", length_pass)
            break
        else:
            print("Введёна НЕ корретная длина пароля")
            print("Попробуйте снова")

def return_chars(): # функция для создания строки для выбора символов для пароля
    chars = ''
    if add_digit():
        chars += digits
    if add_lower_ch():
        chars += lowercase_letters
    if add_upper_ch():
        chars += uppercase_letters
    if add_special_ch():
        chars += punctuation
    if len(chars) == 0:
        print("Вы везде указали - НЕТ - система создаст пароль на основе цифв, прописных букв и спец. символов!")
        chars = digits + lowercase_letters + punctuation    
    return chars

def choise(number): # функция для рандома числа
    rand = random.randrange(1, number)
    return rand

def generate_password(length_pass, string_for_pass): # функция для генерации самого пароля
    password = ''
    for _ in range(1, length_pass+1):
        password += string_for_pass[choise(len(string_for_pass))]
    return password      

string_for_pass = return_chars()
length_pass = len_pass()
password = generate_password(length_pass, string_for_pass)
print(colored("Ваш сгенерированный пароль -->> ", 'red'), password)
