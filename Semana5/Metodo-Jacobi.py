import numpy as np

# Definir la matriz de coeficientes
A = np.array([[4.0, 1.0, -1.0],
              [2.0, 3.0, 0.0],
              [1.0, -1.0, 4.0]])


# Definir el vector de términos independientes
b = np.array([1.0, 2.0, 4.0])

# Adivinar una solución inicial
x0 = np.zeros_like(b)

# Definir el número máximo de iteraciones
max_iter = 100

# Definir la tolerancia
tol = 1e-6

# Realizar el método de Jacobi
for i in range(max_iter):
    # Calcular la nueva solución
    x = np.zeros_like(x0)
    for j in range(A.shape[0]):
        x[j] = (b[j] - np.dot(A[j,:], x0) + A[j,j]*x0[j]) / A[j,j]
    
    # Imprimir los valores de las variables en esta iteración
    print("Iteración", i+1, ": x =", x)
    
    # Comprobar si se ha alcanzado la tolerancia
    if np.allclose(x, x0, rtol=tol):
        break
    
    # Actualizar la solución anterior
    x0 = x.copy()
