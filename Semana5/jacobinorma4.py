import numpy as np

def jacobi(A, b, tol=1e-10, max_iterations=25, x=None):
    """
    Resuelve la ecuación Ax=b mediante el método iterativo de Jacobi con un criterio de parada basado en la tolerancia y la norma 4.
    """
    # Crea una suposición inicial si no se proporciona
    if x is None:
        x = np.zeros(len(A[0]))

    # Divide la matriz A en dos matrices separadas: D y R
    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(max_iterations):
        x_old = x.copy()  # Guarda la aproximación anterior
        x = (b - np.dot(R, x)) / D

        # Calcula la norma 4 del vector de diferencia
        norm_4 = np.linalg.norm(x - x_old, 4)

        # Formatea la norma en notación científica
        formatted_norm = format(norm_4, ".10e")

        # Calcula el error como la norma infinita de la diferencia
        error = np.linalg.norm(x - x_old, np.inf)

        # Formatea el error en notación científica
        formatted_error = format(error, ".10e")

        # Imprime la aproximación, la norma y el error en la iteración actual
        print(f"Iteración {i+1}: {', '.join([format(val, '.10f') for val in x])}, Norma 4: {formatted_norm}, Error: {formatted_error}")

        # Verifica el criterio de parada
        if norm_4 < tol:
            print(f"Convergencia alcanzada con tolerancia {tol} después de {i+1} iteraciones.")
            break

    return x

# Ejemplo de uso
A = np.array([[0.6, 0.3, 0.25],
              [0.2, 0.45, 0.2],
              [0.2, 0.25, 0.55]])

b = np.array([5700, 5800, 4800])

# Suposición inicial (opcional)
guess = np.array([2000, 2000, 2000])

print("\nMatriz A:")
print(A)
print("Vector b:")
print(b)
print("Aproximacion:")
print(guess)
print()
# Tolerancia para el criterio de parada
tolerance = 1e-4

# Calcula la solución
sol = jacobi(A, b, tol=tolerance, x=guess)

# Formatea la solución final antes de imprimir
formatted_sol = [f"{val:.10f}" for val in sol]

print("\nSolución x:")
print(formatted_sol)
