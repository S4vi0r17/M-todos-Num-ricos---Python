import math

def f(x, y):
    return x + y  # Ecuación diferencial: y' = x + y

def exact_solution(x):
    return -x + 2 * math.exp(x) - 1  # Solución exacta de la EDO

def runge_kutta_second_order(x0, y0, h, xn):
    results = [("n", "xn", "yn", "k1", "k2", "y(t)")]
    n = 0
    
    results.append((n, round(x0, 2), round(y0, 6), "-", "-", round(exact_solution(x0), 6)))  # Condición inicial: (n=0, x0, y0)

    while x0 < xn:
        k1 = h * f(x0, y0)  # Primer valor k1
        k2 = h * f(x0 + h, y0 + k1)  # Segundo valor k2
        
        y0 += (k1 + k2) / 2  # Actualización de y0 usando k1 y k2
        x0 += h  # Actualización del valor de x0
        n += 1

        results.append((n, round(x0, 2), round(y0, 6), round(k1, 6), round(k2, 6), round(exact_solution(x0), 6)))  # Resultados de la iteración
        
    return results

# Valores iniciales y parámetros necesarios para el método Runge-Kutta
x0 = 0  # Punto inicial x0
y0 = 1  # Valor inicial y0
xn = 1  # Punto final xn
h = 0.1  # Tamaño de paso h

# Llamada a la función Runge-Kutta de segundo orden
iteration_results = runge_kutta_second_order(x0, y0, h, xn)

# Mostrar los resultados en forma de tabla
print("Iteraciones:")
for row in iteration_results:
    print("{:<3} {:<5} {:<9} {:<12} {:<12} {:<12}".format(*row))
