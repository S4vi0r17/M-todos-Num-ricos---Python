import math

def f(t, y):
    return 0.01 * (70 - y) * (50 - y)

def exact_solution(t):
    return math.exp(-t) + t  # Solución exacta de la EDO

def runge_kutta_fourth_order(x0, y0, h, xn):
    results = [("n", "xn", "yn", "k1", "k2", "k3", "k4", "y(t)")]
    n = 0
    
    results.append((n, round(x0, 2), round(y0, 6), "-", "-", "-", "-", round(exact_solution(x0), 6)))  # Condición inicial: (n=0, x0, y0)
    
    while x0 < xn:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3) 
        
        y0 += (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 += h
        n += 1

        results.append((n, round(x0, 2), round(y0, 6), round(k1, 6), round(k2, 6), round(k3, 6), round(k4, 6), round(exact_solution(x0), 6)))
        
    return results

# Valores iniciales y parámetros necesarios para el método Runge-Kutta
x0 = 0  # Punto inicial x0
y0 = 0  # Valor inicial y0
xn = 25  # Punto final xn
h = 0.1  # Tamaño de paso h

# Llamada a la función Runge-Kutta de cuarto orden
iteration_results = runge_kutta_fourth_order(x0, y0, h, xn)

print("Iteraciones:")
for row in iteration_results:
    print("{:<3} {:<5} {:<9} {:<12} {:<12} {:<12} {:<12} {:<12}".format(*row))
