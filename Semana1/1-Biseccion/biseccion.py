import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.exp(-x) - x


def max_iteraciones(a, b, tol):
    it = math.log((b - a) / (2 * tol)) / math.log(2)
    return math.ceil(it)


def biseccion(a, b, max_iter):

    if f(a) * f(b) >= 0:
        print("No hay cambio de signo...")
        return None
    
    # Mostrar datos de la tabla
    print("Iteración|\ta\t|\tc\t|\tb\t|\tf(a)\t|\tf(c)\t|\tf(b)")

    iteracion = 0
    while iteracion <= max_iter:
        c = (a + b) / 2

        aS = "-" if f(a) < 0 else "+"
        cS = "-" if f(c) < 0 else "+"
        bS = "-" if f(b) < 0 else "+"


        # Mostrar datos de la tabla con 5 decimales
        print(
            f"{iteracion}\t |\t{a:.5f}\t|\t{c:.5f}\t|\t{b:.5f}\t|\t{aS}\t|\t{cS}\t|\t{bS}"
        )

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
max_iteraciones = max_iteraciones(a, b, tolerancia)


if __name__ == "__main__":
    # Graficamos la función en el intervalo [-1.0, 2.0]
    x = np.linspace(a, b, 100)  # Creamos un vector de 100 puntos equiespaciados
    y = f(x)  # Evaluamos la función en cada punto del vector x

    plt.plot(x, y)  # Graficamos la función

    plt.grid()  # Agregamos una cuadrícula
    plt.show()  # Mostramos la gráfica

    resultado = biseccion(a, b, max_iteraciones)

    if resultado is not None:
        print("\nLa raíz aproximada es:", resultado)
    else:
        print(
            "No se encontró una raíz en el intervalo dado con la tolerancia especificada."
        )
