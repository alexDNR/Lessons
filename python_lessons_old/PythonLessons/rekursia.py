def matryoshka (n):
    if n == 1:
        print("Матрёшечка")
    else:
        print("Вверх матрёшки n= ", n)
        matryoshka(n-1)
        print("Низ матрёшки n= ", n)



def pow(a, n):
    """Функция быстрого возведения в степень n, числа а"""
    assert a > 0, "Число должно быть больше 0"
    return (1 if n == 0 else pow(a, n-1)*a)
