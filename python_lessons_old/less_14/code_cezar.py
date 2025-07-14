'''
    Шифр Цезаря 🌶️
Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет древним традициям 
и использует шифр Цезаря. Это их и подвело, ведь данный шифр очень простой. 
Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира, 
поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения. 
Напишите программу для декодирования этого шифра.
    Формат входных данных
В первой строке дается число n (1 ≤ n ≤ 25) – сдвиг, во второй строке даётся закодированное 
сообщение в виде строки со строчными латинскими буквами.
    Формат выходных данных
Программа должна вывести одну строку – декодированное сообщение. 
Обратите внимание, что нужно декодировать сообщение, а не закодировать.
'''
# n = int(input())
# s = input()
# for i in s:
#     decr = ord(i) - n
#     if decr < 97:
#         decr += 26 # букв в английском алфавите
#     print(chr(decr), end="")  

'''
Зашифруйте текст "Блажен, кто верует, тепло ему на свете!" алгоритмом Цезаря с сдвигом вправо на 10 символов.
Примечание. Считайте, что русский алфавит состоит из 32 букв (буква ё отсутствует).
Большие буквы с 1040 по 1071
Малые буквы с 1072 по 1103
spisok = [int(i) for i in range(ord("а"), ord("я") + 1)]
print(spisok) # проверка на код русских букв
'''
# s = "Блажен, кто верует, тепло ему на свете!"
# descriptyon_str = ''
# n = 10
# for i in s:
#     if 1040 <= ord(i) <= 1103:
#         if i.isupper():
#             desc = ord(i)+n
#             descriptyon_str += chr(desc)
#         elif i.islower():
#             desc = ord(i)+n
#             descriptyon_str += chr(desc)
#     else:
#         descriptyon_str += i        
# print(descriptyon_str)              


'''
Зашифруйте текст "To be, or not to be, that is the question!" 
алгоритмом Цезаря с сдвигом вправо на 17 символов.
a-z = 97-122
A-Z = 65-90
'''
# s = "To be, or not to be, that is the question!"
# descriptyon_str = ''
# n = 17
# for i in s.lower():
#     if 97 <= ord(i) <= 122:
#         desc = ord(i) + n
#         if desc > 122:
#             desc -= 26
#             descriptyon_str += chr(desc)  
#         else:
#             descriptyon_str += chr(desc)     
#     else:
#         descriptyon_str += i        
# print(descriptyon_str.capitalize())


'''
Текст "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг." 
был получен в результате шифрования алгоритмом Цезаря с сдвигом вправо на 7 символов.
 Расшифруйте данный текст.
Примечание. Считайте, что русский алфавит состоит из 32 букв (буква ё отсутствует).
'''
# s = "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
# descriptyon_str = ''
# n = 7
# for i in s.lower():
#     if 1072 <= ord(i) <= 1103:
#             desc = ord(i)-n
#             if desc < 1072:
#                 desc +=32
#                 descriptyon_str += chr(desc)
#             else:
#                 descriptyon_str += chr(desc)    
#     else:
#         descriptyon_str += i        
# print(descriptyon_str.capitalize())   


'''
Текст "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd." 
был получен в результате шифрования алгоритмом Цезаря со сдвигом вправо на 25 символов. 
Расшифруйте данный текст.
'''
# s = "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd."
# descriptyon_str = ''
# n = 25
# for i in s.lower():
#     if 97 <= ord(i) <= 122:
#         desc = ord(i) - n
#         if desc < 97:
#             desc += 26
#             descriptyon_str += chr(desc)  
#         else:
#             descriptyon_str += chr(desc)     
#     else:
#         descriptyon_str += i        
# print(descriptyon_str.capitalize())


'''
Текст "Hawnj pk swhg xabkna ukq nqj." 
был получен в результате шифрования алгоритмом Цезаря с сдвигом вправо на nn символов. 
Расшифруйте данный текст.
Примечание. Считайте, что n∈[0;25].
'''
# s = "Hawnj pk swhg xabkna ukq nqj."
# for j in range(26):
#     descriptyon_str = ''
#     for i in s.lower():
#         if 97 <= ord(i) <= 122:
#             desc = ord(i) - j
#             if desc < 97:
#                 desc += 26
#                 descriptyon_str += chr(desc)  
#             else:
#                 descriptyon_str += chr(desc)     
#         else:
#             descriptyon_str += i        
#     print(descriptyon_str.capitalize())
#     print()


'''
    Аве, Цезарь 🌶️
На вход программе подается строка текста на английском языке, 
в которой нужно зашифровать все слова. 
Каждое слово строки следует зашифровать с помощью шифра Цезаря 
(циклического сдвига на длину этого слова). 
Строчные буквы при этом остаются строчными, а прописные – прописными.
    Формат входных данных 
На вход программе подается строка текста на английском языке.
    Формат выходных данных
Программа должна вывести зашифрованный текст в соответствии с условием задачи.
Примечание. Символы, не являющиеся английскими буквами, не изменяются.
Day, mice. "Year" is a mistake!
a-z = 97-122
A-Z = 65-90
#         desc = ord(i) + n
#         if desc > 122:
#             desc -= 26
'''
# функция определения длины слова без спец. символов
def len_word(word): 
    count = 0
    for i in word:
        if i.isalpha():
            count += 1
    return count        

s = input().split()
descriptyon_str = '' # пустая строка для вывода
for i in s: # цикл по всем словам в строке
    n = len_word(i) # записываем в переменную длину слова, которая будет смещением в кодировании
    for j in i: # цикл по буквам в каждом слове
        if j.isalpha(): # если элемент - буква
            if 65 <= ord(j) <= 90: # проверка для заглавных букв
                desc = ord(j) + n # смещение
                if desc > 90:
                    desc -= 26
                    descriptyon_str += chr(desc)
                else:
                    descriptyon_str += chr(desc)
            elif 97 <= ord(j) <= 122: # проверка для прописных букв
                desc = ord(j) + n 
                if desc > 122:
                    desc -= 26
                    descriptyon_str += chr(desc)
                else:
                    descriptyon_str += chr(desc)
        else:
            descriptyon_str += j # если не буква, то просто записываем этот символ 
    descriptyon_str += ' ' # после слова ставим пробел                            
print(descriptyon_str)


