import numpy as np

A = np.array([[1.0, 1.0, 1.0], [0.0, 2.0, -1.0], [3.0, -2.0, 1.0]])

b = np.array([6.0, 3.0, 4.0])

AB = np.column_stack((A, b))

filas, columnas = AB.shape

# Eliminación gaussiana (inferior)

def sustitucion_hacia_adelante(matriz, vector):
    n = len(vector)
    x = np.zeros(n)

    for i in range(n):
        suma = np.dot(matriz[i, :i], x[:i])
        x[i] = (vector[i] - suma) / matriz[i, i]

    return x

solucion = sustitucion_hacia_adelante(A_escalonada, b_escalonado)  # Utiliza A_escalonada y b_escalonado aquí

print("Solución:", solucion)
