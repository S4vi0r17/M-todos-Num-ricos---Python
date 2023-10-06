import numpy as np

def gauss_seidel(A, b, tol=1e-10, max_iterations=25, x=None):
    """
    Resuelve la ecuación Ax=b mediante el método iterativo de Gauss-Seidel con un criterio de parada basado en la tolerancia.
    """
    # Crea una suposición inicial si no se proporciona
    if x is None:
        x = np.zeros(len(A[0]))

    for i in range(max_iterations):
        x_old = x.copy()  # Guarda la aproximación anterior

        for j in range(len(x)):
            # Calcula la suma de los términos de la fila actual sin el término correspondiente a x_j
            row_sum = np.dot(A[j, :j], x[:j]) + np.dot(A[j, j+1:], x_old[j+1:])
            x[j] = (b[j] - row_sum) / A[j, j]

        # Calcula el error como la norma infinita de la diferencia
        error = np.linalg.norm(x - x_old, np.inf)

        # Formatea el error en notación científica
        formatted_error = format(error, ".10e")

        # Imprime la aproximación y el error en la iteración actual
        print(f"Iteración {i+1}: {', '.join([format(val, '.10f') for val in x])}, Error: {formatted_error}")

        # Verifica el criterio de parada
        if error < tol:
            print(f"Convergencia alcanzada con tolerancia {tol} después de {i+1} iteraciones.")
            break

    return x

# Ejemplo de uso
A = np.array([[4.0, 2.0, -1.0],
              [-2.0, 5.0, 2.0],
              [-6.0, 3.0, 7.0]])

b = np.array([-3.0, -9.0, 10.0])

# Suposición inicial (opcional)
guess = np.array([1.0, -2.0, 3.0])

print("\nMatriz A:")
print(A)
print("Vector b:")
print(b)

# Tolerancia para el criterio de parada
tolerance = 1e-4

# Calcula la solución
sol = gauss_seidel(A, b, tol=tolerance, x=guess)

# Formatea la solución final antes de imprimir
formatted_sol = [f"{val:.10f}" for val in sol]

print("\nSolución x:")
print(formatted_sol)
