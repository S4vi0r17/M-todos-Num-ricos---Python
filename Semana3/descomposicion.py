import numpy as np

def LU_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for k in range(n):
        # Calcula los elementos de la matriz U
        U[k, k:] = A[k, k:] - np.dot(L[k, :k], U[:k, k:])
        
        # Calcula los elementos de la matriz L
        L[k+1:, k] = (A[k+1:, k] - np.dot(L[k+1:, :k], U[:k, k])) / U[k, k]

        # Imprime los pasos en cada iteración
        print(f'Iteración {k + 1}:\n')
        print(f'Matriz L:\n{L}\n')
        print(f'Matriz U:\n{U}\n')

    return L, U

# Ejemplo de uso
A = np.array([[4.0, 3.0, 2.0],
              [2.0, 2.0, 3.0],
              [3.0, 4.0, 5.0]])




L, U = LU_decomposition(A)
print(f'Matriz L final:\n{L}\n')
print(f'Matriz U final:\n{U}\n')
