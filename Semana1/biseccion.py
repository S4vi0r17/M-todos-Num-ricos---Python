import math

def f(x):
    return math.exp(-x) - x

def max_iteraciones(a,b,tol):
    it = math.log((b-a)/(2*tol))/math.log(2)
    return math.ceil(it)

def biseccion(a, b, tol, max_iter):
    print("Las iteraciones son: ",max_iter)
    if f(a) * f(b) >= 0:
        print("No hay cambio de signo...")
        return None

    iteracion = 0
    while iteracion <= max_iter:
        c = (a + b) / 2

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iteracion += 1

    return c

# Parámetros iniciales
a = 0.0
b = 1.0
tolerancia = 1e-3
max_iteraciones = max_iteraciones(a,b,tolerancia)



if __name__ == "__main__":

    resultado = biseccion(a, b, tolerancia, max_iteraciones)
    if resultado is not None:
        print("La raíz aproximada es:", resultado)
    else:
        print("No se encontró una raíz en el intervalo dado con la tolerancia especificada.")