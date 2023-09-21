import numpy as np

A = np.array([[1.0, 0.0, 0.0], [0.5, 1.0, 0.0], [2.0, 2.0, 1.0]])

b = np.array([2.0, 2.0, 4.0])

def sustitucion_hacia_adelante(matriz, vector):
    n = len(vector)
    x = np.zeros(n)

    for i in range(n):
        suma = np.dot(matriz[i, :i], x[:i])
        x[i] = (vector[i] - suma) / matriz[i, i]

    return x

solucion = sustitucion_hacia_adelante(A, b)

print("Solución:", solucion)
