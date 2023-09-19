import math

def punto_fijo(g, x0, tol, max_iter):

    # Inicializar variables
    iteracion = 0
    x = x0

    while iteracion < max_iter:
        x_nuevo = g(x)  # Aplicar la función de punto fijo

        # Imprimir información de la iteración
        print("Iteración:", iteracion, "\tx:", x_nuevo)

        # Verificar la convergencia
        if abs(x_nuevo - x) < tol:
            return x_nuevo

        x = x_nuevo
        iteracion += 1

# Ejemplo de uso:
def g(x):
    return (1/3) * math.sqrt((60)/(math.pi) + x**3)

x0 = 1
tolerancia = 1e-3
max_iteraciones = 7

raiz = punto_fijo(g, x0, tolerancia, max_iteraciones)
print("La raíz aproximada es:", raiz)
