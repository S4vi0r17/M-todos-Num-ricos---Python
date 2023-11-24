import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Método de Euler modificado para resolver la EDO
def euler_modified(f, x0, y0, x1, n):
    h = (x1 - x0) / n
    xi = np.zeros(n + 1)
    yi = np.zeros(n + 1)
    xi[0] = x0
    yi[0] = y0

    for i in range(n):
        xi[i + 1] = xi[i] + h
        fn = f(xi[i], yi[i])
        fn_plus_1 = f(xi[i + 1], yi[i] + h * fn)
        yi[i + 1] = yi[i] + h * (fn + f(xi[i + 1], yi[i] + h * fn)) / 2

    return xi, yi

# Función de la EDO: y' = 1 + t - y
def f(t, y):
    return 1 + t - y

# Solución exacta de la EDO
def exact_solution(t):
    return np.exp(-t) + t

def main():
    x0 = 0
    y0 = 1
    x1 = 0.5
    n = 5

    x, y = euler_modified(f, x0, y0, x1, n)
    exact_y = exact_solution(x)

    errors = np.abs(y - exact_y)  # Cálculo de los errores

    # Creación del DataFrame con los resultados
    df = pd.DataFrame({
        'n': np.arange(n + 1),
        't_n': x,
        'y_n (Euler mod.)': y,
        'y(t_n) (exacta)': exact_y,
        'Error': errors
    })

    print(df)

    fig = plt.figure()
    plt.plot(x, y, 'o--', label='Euler modificado')
    plt.plot(x, exact_y, label='Solución exacta', linestyle='--')
    plt.grid()
    plt.legend()
    plt.title('Euler modificado vs Solución exacta')
    plt.xlabel('tiempo')
    plt.ylabel('Concentración')
    plt.show()
    fig.savefig("edo_euler_mod5_exact.pdf", bbox_inches='tight')


if __name__ == "__main__":
    main()
