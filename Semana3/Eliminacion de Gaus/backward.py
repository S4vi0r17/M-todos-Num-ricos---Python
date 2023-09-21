import numpy as np

A = np.array([[1.0, 2.0, -1.0], [0.0, 1.0, 1.0], [0.0, 0.0, 2.0]])

b = np.array([2.0, 2.0, 2.0])

# Combinamos la matriz A y el vector b en una única `matriz aumentada`
AB = np.column_stack((A, b))

filas, columnas = AB.shape

for i in range(min(filas, columnas)):
    pivote = AB[i, i]

    if pivote == 0:
        for j in range(i + 1, filas):
            if AB[j, i] != 0:
                AB[[i, j]] = AB[[j, i]]
                pivote = AB[i, i]

    # Realiza la eliminación gaussiana en esta columna
    for j in range(i + 1, filas):
        factor = AB[j, i] / pivote
        AB[j, i:] -= factor * AB[i, i:]

# Ahora, separamos la matriz escalonada en una matriz y un vector
A = AB[:, :-1]
b = AB[:, -1]

# Método de sustitución hacia atrás


def backward_substitution(A, b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        suma = np.dot(A[i, i + 1:], x[i + 1:])
        x[i] = (b[i] - suma) / A[i, i]
    return x


x = backward_substitution(A, b)

print("Matriz escalonada:")
print(A)
print("\nVector b escalonado:")
print(b)
print("\nSolución:")
print(x)
