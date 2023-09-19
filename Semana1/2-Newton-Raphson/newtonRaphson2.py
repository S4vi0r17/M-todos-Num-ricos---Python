import numpy as np

def f(x):
    return np.exp(-x) - x

def df(x):
    return -np.exp(-x) - 1

def newton_raphson(f, df, x0, tol):

    if abs(f(x0)) < tol:
        return x0
    else:
        return newton_raphson(f, df, x0 - f(x0)/df(x0), tol)

# Ejemplo de uso del método de Newton-Raphson
x0 = 1.5
tol = 1e-6

estimate = newton_raphson(f, df, x0, tol)
print("The estimated root is:", estimate)
