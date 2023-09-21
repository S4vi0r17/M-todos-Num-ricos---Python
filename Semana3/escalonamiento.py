import numpy as np

A = np.array(
    [
        [1.0, 2.0, 0.0, -1.0],
        [0.0, 0.0, 1.0, 1.0],
        [0.0, 0.0, 4.0, -3.0],
        [0.0, 2.0, 0.0, 1.0],
    ]
)

b = np.array([2.0, 2.0, 1.0, 3.0])

# Combinamos la matriz A y el vector b en una única `matriz aumentada`
AB = np.column_stack((A, b))

# Obtenemos las dimensiones de la matriz aumentada
filas, columnas = AB.shape

# Eliminación gaussiana
for i in range(min(filas, columnas - 1)):
    # Pivote en la diagonal
    pivote = AB[i, i]

    # Si pivote = 0, intercambiamos filas
    if pivote == 0:
        for j in range(i + 1, filas):
            if AB[j, i] != 0:
                AB[[i, j]] = AB[
                    [j, i]
                ]  # Este procedimiento intercambia filas y es propio de NumPy
            pivote = AB[i, i]

    # Realiza la eliminación gaussiana en esta columna
    for j in range(i + 1, filas):
        factor = AB[j, i] / pivote
        AB[j, i:] -= factor * AB[i, i:]

# Ahora, separamos la matriz escalonada en una matriz y un vector
A_escalonada = AB[:, :-1]  # Todas las filas, todas las columnas menos la última
b_escalonado = AB[:, -1]  # Todas las filas, sólo la última columna

print("Matriz escalonada:")
print(A_escalonada)
print("\nVector b escalonado:")
print(b_escalonado)
