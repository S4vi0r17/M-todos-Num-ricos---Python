import math

def f(t, y):
    return 1 + t - y

def exact_solution(t):
    return math.exp(-t) + t

def runge_kutta_fourth_order(x0, y0, h, xn):
    results = [("n", "xn", "yn", "k1", "k2", "k3", "k4", "y(t)")]
    n = 0
    
    results.append((n, round(x0, 2), round(y0, 6), "-", "-", "-", "-", round(exact_solution(x0), 6)))
    
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

# Valores iniciales
x0 = 0
y0 = 1
xn = 0.5
h = 0.1

iteration_results = runge_kutta_fourth_order(x0, y0, h, xn)

# Mostrar los resultados en forma de tabla
print("Iteraciones:")
for row in iteration_results:
    print("{:<3} {:<5} {:<9} {:<12} {:<12} {:<12} {:<12} {:<12}".format(*row))
