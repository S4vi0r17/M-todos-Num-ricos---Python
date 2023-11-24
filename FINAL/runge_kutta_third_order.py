import math

def f(t, y):
    return 1 + t - y

def exact_solution(t):
    return math.exp(-t) + t

def runge_kutta_third_order(t0, y0, h, tn):
    results = [("n", "tn", "yn", "k1", "k2", "k3", "y(t)")]
    n = 0

    results.append((n, round(t0, 2), round(y0, 6), "-", "-", "-", round(exact_solution(t0), 6)))

    while t0 < tn:
        k1 = h * f(t0, y0)
        k2 = h * f(t0 + h/2, y0 + k1/2)
        k3 = h * f(t0 + h, y0 - k1 + 2*k2)
        
        y0 += (k1 + 4*k2 + k3) / 6
        t0 += h
        n += 1

        results.append((n, round(t0, 2), round(y0, 6), round(k1, 6), round(k2, 6), round(k3, 6), round(exact_solution(t0), 6)))
        
    return results

# Valores iniciales
t0 = 0 # t0 = x0
y0 = 1 # y0 = y(x0)
tn = 0.5 # tn = xn
h = 0.1 # h = (xn - x0) / n

iteration_results = runge_kutta_third_order(t0, y0, h, tn)

# Mostrar los resultados en forma de tabla
print("Iteraciones:")
for row in iteration_results:
    print("{:<3} {:<5} {:<9} {:<12} {:<12} {:<12} {:<12}".format(*row))
