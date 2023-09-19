import math

def secante(func, x0, x1, tol):

    while True:
    
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))

        # Error relativo
        error = abs(x2 - x1) / abs(x2)

        # Mostrar la información de la iteración y el error relativo en notación científica
        print(f"{x2:.10f}\t{error:.10e}")
        # el .10f redondera a 10 decimales
        
        if error < tol:
            return x2

        # Actualizar las aproximaciones anteriores
        x0 = x1
        x1 = x2

# Ejemplo de uso:
def f(x):
    return math.exp(-x) - x

x0 = 0.5
x1 = 1.0
tolerancia = 1e-6

print("raíz\t\terror relativo")

raiz = secante(f, x0, x1, tolerancia)
print("La raíz aproximada es:", raiz)