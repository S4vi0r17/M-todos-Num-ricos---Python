import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x * (18-2*x) * (14-2*x) - 100


def max_iteraciones(a, b, tol):
    it = math.log((b - a) / (2 * tol)) / math.log(2)
    print("Iteraciones necesarias:", math.ceil(it))
    return math.ceil(it)


def biseccion(a, b, max_iter):

    if f(a) * f(b) >= 0:
        print("No hay cambio de signo...")
        return None
    
    # Mostrar datos de la tabla
    print("Iteración|\ta\t\t|\tc\t\t|\tb\t\t|\tf(a)\t|\tf(c)\t|\tf(b)")

    iteracion = 0
    while iteracion <= max_iter:
        c = (a + b) / 2

        aS = "-" if f(a) < 0 else "+"
        cS = "-" if f(c) < 0 else "+"
        bS = "-" if f(b) < 0 else "+"


        # Mostrar datos de la tabla con 5 decimales
        print(
            f"{iteracion}\t |\t{a:.6f}\t|\t{c:.6f}\t|\t{b:.6f}\t|\t{aS}\t|\t{cS}\t|\t{bS}"
        )

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        # print("\nf(c): ",f(c))
        # print(f"Error: {abs(f(c)):.6f}")
        if f(c) == 0:
            return c

        iteracion += 1

    return c


# Parámetros iniciales
a = 4
b = 6
tolerancia = 1e-4
max_iter = max_iteraciones(a, b, tolerancia)


if __name__ == "__main__":
    # Graficamos la función en el intervalo [-1.0, 2.0]
    x = np.linspace(-4, 10, 1000)  # Creamos un vector de 100 puntos equiespaciados
    y = f(x)  # Evaluamos la función en cada punto del vector x

    plt.plot(x, y)  # Graficamos la función

    plt.grid()  # Agregamos una cuadrícula
    plt.show()  # Mostramos la gráfica

    resultado = biseccion(a, b, max_iter)

    if resultado is not None:
        print("\nLa raíz aproximada es:", resultado)
    else:
        print(
            "No se encontró una raíz en el intervalo dado con la tolerancia especificada."
        )
