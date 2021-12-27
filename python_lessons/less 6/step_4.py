'''
    Две старушки
Две старушки идут навстречу друг другу с постоянными скоростями V1 и V2 км/ч. 
Определите, через какое время старушки встретятся, если расстояние между ними равно S км.

    Формат входных данных
На вход программе подаются три числа с плавающей точкой S, V1, V2, каждое на отдельной строке.

    Формат выходных данных 
Программа должна вывести одно число в соответствии с условием задачи.

Примечание. Это очень быстрые старушки.
'''
s = float(input())
v1 = float(input())
v2 = float(input())
# для посчёта времени встерчи необходимо посчитать скорость
# сближения двух бабушек - v = v1 + v2. Время будет t = S / V
v = v1 + v2
t = s / v
print(t)

# урок пройден