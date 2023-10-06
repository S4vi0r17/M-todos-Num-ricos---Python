import numpy as np

# Definir la matriz de coeficientes y el vector de términos independientes
A = np.array([[5.0, -1.0, 1.0, 1.0],
              [1.0, 4.0, 0.0, 1.0],
              [3.0, -1.0, 6.0, 0.0],
              [0.0, 1.0, -1.0, 3.0]])

b = np.array([5.0, 2.0, -3.0, 4.0])

# Definir la matriz diagonal y la matriz de coeficientes sin la diagonal
D = np.diag(np.diag(A))
R = A - D

# Definir el vector de solución inicial y el número máximo de iteraciones
x0 = np.zeros_like(b)
max_iter = 100

# Implementar el método de Jacobi
for i in range(max_iter):
    x = (b - np.dot(R, x0)) / np.diag(D)
    if np.allclose(x, x0, rtol=1e-10):
        break
    x0 = x

print("La solución del sistema es:", x)
