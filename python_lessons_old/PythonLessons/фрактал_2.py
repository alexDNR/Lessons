import graphics as gr
window = gr.GraphWin("Фрактал", 800, 700)



def fractal_rectangle(A, B, C, D, E, F, deep = 20):
    alpha = 0.1
    if deep < 1:
        return
    for M,N in [(A, B), (B, C), (C, D), (D, E), (E, F), (F, A)]:
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
    B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
    C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
    D1 = (D[0]*(1-alpha) + E[0]*alpha, D[1]*(1-alpha) + E[1]*alpha)
    E1 = (E[0]*(1-alpha) + F[0]*alpha, E[1]*(1-alpha) + F[1]*alpha)
    F1 = (F[0]*(1-alpha) + A[0]*alpha, F[1]*(1-alpha) + A[1]*alpha)

    fractal_rectangle(A1, B1, C1, D1, E1, F1, deep-1)
    

fractal_rectangle((300, 100), (600, 100), (750, 325), (600, 600), (300, 600), (150, 325), 100)
