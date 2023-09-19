import math

def f(x):
    return math.exp(-x) - x

def bisection(f, a, b, tol):
    if f(a) * f(b) > 0:
        print("El método de bisección no garantiza convergencia en este intervalo.")
        return None
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2



if __name__ == "__main__":

    a = 0
    b = 1
    tolerancia = 1e-3

    raiz_aproximada = bisection(f, a, b, tolerancia)
    print("La raíz aproximada es:", raiz_aproximada)
