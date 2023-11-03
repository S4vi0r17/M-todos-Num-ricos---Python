def diferencia_finita_progresiva(f, x, h, order):
    if order == 0:
        return f(x)
    else:
        return diferencia_finita_progresiva(f, x + h, h, order - 1) - diferencia_finita_progresiva(f, x, h, order - 1)

# Función dada
def f(x):
    return x**3 - x + 2

# Tamaño del incremento (h)
h = 1

# Valores de xi
xi_values = [0, 1, 2, 3, 4]

# Calcular Δ^0 f(xi), Δ^1 f(xi), Δ^2 f(xi) y Δ^3 f(xi) para cada xi
delta_values = []

for xi in xi_values:
    delta0 = diferencia_finita_progresiva(f, xi, h, 0)
    delta1 = diferencia_finita_progresiva(f, xi, h, 1)
    delta2 = diferencia_finita_progresiva(f, xi, h, 2)
    delta3 = diferencia_finita_progresiva(f, xi, h, 3)
    
    delta_values.append((delta0, delta1, delta2, delta3))

# Imprimir la tabla de resultados
print("xi       Δ^0 f(xi)       Δ^1 f(xi)       Δ^2 f(xi)       Δ^3 f(xi)")
for xi, deltas in zip(xi_values, delta_values):
    print(f"{xi}        {deltas[0]:.2f}             {deltas[1]:.2f}            {deltas[2]:.2f}          {deltas[3]:.2f}")
