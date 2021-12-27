'''
Переведите двоичное число 111111_2 в десятичную систему счисления.
'''
# numbers = '111111'
# stepen = len(numbers)-1
# total = 0
# for i in numbers:
#     total += int(i)*2**stepen
#     print("Сумма = ", total, "И степень числа =", stepen)
#     stepen -= 1
# print(total)    


'''
Переведите шестнадцатеричное число 1AF2_{16} в десятичную систему счисления.
'''                                                 
# number = '1AF2'
# total = 0
# for i in range(len(number)):
#     if number[i]=='A':
#         total += 10*(16**(len(number)-i-1))
#     elif number[i] == 'B':
#         total += 11*(16**(len(number)-i-1))
#     elif number[i] == 'C':
#         total += 12*(16**(len(number)-i-1))
#     elif number[i] == 'D':
#         total += 13*(16**(len(number)-i-1))
#     elif number[i] == 'E':
#         total += 14*(16**(len(number)-i-1))    
#     elif number[i] == 'F':
#         total += 15*(16**(len(number)-i-1))
#     else:
#         total += int(number[i])*16**(len(number)-i-1)
# print(total)