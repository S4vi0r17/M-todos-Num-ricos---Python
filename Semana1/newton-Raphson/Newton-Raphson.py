# Metodo: Newton-Raphson

import numpy as np

def f(x):
    return np.exp(-x) - x

def df(x):
    return -np.exp(-x) - 1


print("\nx0\t\tf(x0)\t\tf'(x0)\t\tx1\t\tE(error relativo)")

def newton_raphson(f, df, x0, tol):
    while True:
        x1 = x0 - f(x0) / df(x0)
        
        # Error relativo
        error = abs(x1 - x0) / abs(x1)

        # Mostrar la información de la iteración
        print(f"{x0:.10f}\t{f(x0):.12f}\t{df(x0):.10f}\t{x1:.10f}\t{error:.10f} => {error:.10e}")

        # Verificamo si el error es menor que la tolerancia
        if error < tol:
            return x1
        
        x0 = x1


# Uso del método de Newton-Raphson
x0 = 0.5
tolerance = 1e-3
root = newton_raphson(f, df, x0, tolerance)

print("\nLa raíz aproximada es:", root)
