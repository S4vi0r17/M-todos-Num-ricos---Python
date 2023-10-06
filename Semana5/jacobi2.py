import numpy as np

# Definir la matriz de coeficientes A y el vector de términos constantes B
A = np.array([[4.0, 1.0, -1.0],
              [2.0, 3.0, 0.0],
              [1.0, -1.0, 4.0]])
B = np.array([1.0, 2.0, 4.0])

# Dividir A en las matrices D y R
D = np.diag(np.diag(A))
R = A - D

# Valor inicial para X
X = np.array([0, 0, 0])

# Número de iteraciones
num_iteraciones = 5

# Realizar iteraciones
for i in range(num_iteraciones):
    X_anterior = X.copy()
    
    # Calcular X(k+1) utilizando la fórmula de Jacobi
    X = np.dot(np.linalg.inv(D), B - np.dot(R, X))
    
    print(f"Iteración {i + 1}:")
    print("X(k+1) = ", X)

# Imprimir la solución final
print("\nSolución final:")
print("x = ", X[0])
print("y = ", X[1])
print("z = ", X[2])
