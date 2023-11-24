import pandas as pd
import matplotlib.pyplot as plt

# Definición de la ecuación diferencial dy/dt = 1 + t - y

def f(t, y):
    return 1 + t - y


# Solución exacta de la EDO

def y_exact(t):
    return pow(2.71828, -t) + t


# Método de Euler para resolver la EDO

def euler_method(h, t_end):
    n = int(t_end / h)  # Número de pasos
    data = []

    # Condiciones iniciales
    t = 0.0
    y = 1.0

    for i in range(n + 1):  # Modificado para incluir n=5
        fn = f(t, y)
        y_e = y_exact(t)
        error = abs(y_e - y)  # Cálculo del error

        data.append([i, t, y, fn, y_e, error])

        # Calcular el siguiente paso
        y = y + h * fn
        t = t + h

    # Crear un DataFrame para mostrar los resultados en una tabla
    df = pd.DataFrame(
        data, columns=['n', 't_n', 'y_n', 'f(n)', 'y(t_n)', 'Error'])
    return df


# Parámetros para el método de Euler
h = 0.1
t_end = 0.5

# Obtener los resultados utilizando el método de Euler
results = euler_method(h, t_end)
print(results)