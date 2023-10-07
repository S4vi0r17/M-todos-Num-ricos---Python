import numpy as np

def decomposition(A, b):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # Gaussian elimination
    for k in range(n):
        L[k][k] = 1
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            L[i][k] = factor
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]

        for j in range(k, n):
            U[k][j] = A[k][j]

    # Forward substitution
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
        y[i] /= L[i][i]

    # Backward substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    # Mostrar la matriz inferior L
    print("Matriz inferior L:")
    print(L)

    # Mostrar la matriz superior U
    print("\nMatriz superior U:")
    print(U)

    # Mostrar el valor de y
    print("\nValor de y:")
    print(y)

    return x

A = np.array([[2.0, 1.0, -1.0],
              [1.0, -1.0, 2.0],
              [4.0, -1.0, 1.0]])

b = np.array([2.0, 2.0, 4.0])

resultado = decomposition(A, b)
print("\nResultado final x:")
print(resultado)
