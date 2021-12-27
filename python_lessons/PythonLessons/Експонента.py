def exp (n):
    """
        определение экспоненты числа где e = lim (x --> infinity) (1 + 1/x)^x
        где n - целое число
    """
    
    for i in range (1, n):
        e = (1 + 1/i)**i
        
    print(e)        
