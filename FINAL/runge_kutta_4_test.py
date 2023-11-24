import math

# Definición de la ecuación diferencial: y' = 1 + t - y
def f(t, y):
    return 1 + t - y

# Función de la solución exacta para comparación
def exact_solution(t):
    return math.exp(-t) + t

# Función para resolver la EDO usando Runge-Kutta de cuarto orden
def runge_kutta_fourth_order(x0, y0, h, xn):
    results = [("n", "tn", "yn", "k1", "k2", "k3", "k4", "y(t)")]
    n = 0
    results.append((n, round(x0, 2), round(y0, 6), "-", "-", "-", "-", round(exact_solution(x0), 6)))  # Agregar la condición inicial a los resultados

    while x0 < xn:  # Iterar hasta alcanzar el valor final xn
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)

        y0 += (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 += h
        n += 1

        results.append((n, round(x0, 2), round(y0, 6), round(k1, 6), round(k2, 6), round(k3, 6), round(k4, 6), round(exact_solution(x0), 6)))  # Guardar los resultados de cada iteración
        
    return results

# Valores iniciales y parámetros para el método Runge-Kutta
x0 = 0  # Punto inicial x0
y0 = 1  # Valor inicial y0
xn = 0.5  # Punto final xn
h = 0.1  # Tamaño de paso h

# y' = 1 + t - y
# y(0) = 1
# y(0.5) = ?
# h = 0.1

# Resolver la EDO usando Runge-Kutta de cuarto orden
iteration_results = runge_kutta_fourth_order(x0, y0, h, xn)

# Mostrar las iteraciones en forma de tabla
print("{:<3} {:<5} {:<9} {:<12} {:<12} {:<12} {:<12} {:<12}".format(*iteration_results[0]))  # Encabezados
for row in iteration_results[1:]:
    print("{:<3} {:<5} {:<9} {:<12} {:<12} {:<12} {:<12} {:<12}".format(*row))
