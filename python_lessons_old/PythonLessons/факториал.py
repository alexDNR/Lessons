def factorial(n):
    assert n >= 0, "Факториал отрицательного числа не определён"
    if n == 0:
        return 1
    print(n)
    return factorial(n-1)*n
    
