import numpy as np

# Esto es del ejemplo 3




def differences_progresivas(x, y):
    n = len(x)
    f = np.zeros(n)
    table = np.zeros((n, n))

    for i in range(n):
        f[i] = y[i]
        table[i, 0] = f[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = table[i + 1, j - 1] - table[i, j - 1]

    print("Tabla de Diferencias Progresivas:")
    print("Punto xi | f [xi]  | Δf [xi]  | Δ^2f [xi] | Δ^3f [xi] | Δ^4f [xi]")
    for i in range(n):
        row = [f"{x[i]:.5f}", f"{table[i, 0]:.5f}"]
        for j in range(1, n):
            if i + j < n:
                row.append(f"{table[i, j]:.5f}")
            else:
                row.append("   --   ")
        print(" | ".join(row))

def interpolate(x, y, x_interp):
    n = len(x)
    f = np.zeros(n)
    table = np.zeros((n, n))

    for i in range(n):
        f[i] = y[i]
        table[i, 0] = f[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = table[i + 1, j - 1] - table[i, j - 1]

    result = f[0]
    factor = 1

    for j in range(1, n):
        factor *= (x_interp - x[j - 1]) / (j)
        result += (table[0, j] * factor)

    return result

x = np.array([0, 1, 2, 3])
y = np.array([2, 1.3679, 1.1353, 1.0497])

x_interp = 0.2

differences_progresivas(x, y)
interpolated_value = interpolate(x, y, x_interp)
print(f"\nEl valor interpolado en x = {x_interp:.5f} es {interpolated_value:.5f}")
