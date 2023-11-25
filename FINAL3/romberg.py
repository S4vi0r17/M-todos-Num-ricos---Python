import numpy as np
from tabulate import tabulate  # Librería para mostrar tablas

# Definición de la función f(x)
def f(x):
    return 2**(x**2 - 1)

# Método del trapecio para un número dado de subintervalos
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    return integral * h

# Método de Romberg para aproximar la integral y mostrar los datos en una tabla
def romberg_integration_table(f, a, b, tol=1e-6):
    # Inicialización de la tabla de Romberg
    R = np.zeros((10, 4))

    # Aproximación con un solo paso (h = b - a)
    R[0, 0] = 0.5 * (b - a) * (f(a) + f(b))
    R[0, 1] = trapezoidal_rule(f, a, b, 1)

    for i in range(1, 5):
        # Aproximaciones utilizando el método del trapecio con más subintervalos
        R[i, 0] = 2**i
        R[i, 1] = trapezoidal_rule(f, a, b, 2**i)

        # Cálculo de Sn y Bn
        if i > 0:
            R[i, 2] = (4 * R[i, 1] - R[i - 1, 1]) / 3
        if i > 1:
            R[i, 3] = (16 * R[i, 2] - R[i - 1, 2]) / 15

        # Construcción de la tabla con los datos
        data = R[:i + 1, :]
        table_headers = ["n", "Tn", "Sn", "Bn"]
        print(tabulate(data, headers=table_headers, floatfmt=".10f"))
        print("\n")

        # Condición de convergencia
        if abs(R[i, 2] - R[i, 1]) < tol:
            break

    return R[i, 2]

# Calcular la aproximación del área bajo la curva y mostrar la tabla
approx_area = romberg_integration_table(f, 0, 2)
print("Aproximación del área usando el método de Romberg:", approx_area)


# import numpy as np
# from tabulate import tabulate  # Librería para mostrar tablas

# # Definición de la función f(x)
# def f(x):
#     return 2**(x**2 - 1)

# # Método del trapecio para un número dado de subintervalos
# def trapezoidal_rule(f, a, b, n):
#     h = (b - a) / n
#     integral = 0.5 * (f(a) + f(b))
#     for i in range(1, n):
#         integral += f(a + i * h)
#     return integral * h

# # Método de Romberg para aproximar la integral y mostrar los datos en una tabla
# def romberg_integration_table(f, a, b, tol=1e-6):
#     # Inicialización de la tabla de Romberg
#     R = np.zeros((5, 4))  # Establecer el tamaño de la tabla

#     # Aproximación con un solo paso (h = b - a)
#     R[0, 0] = 0.5 * (b - a) * (f(a) + f(b))
#     R[0, 1] = trapezoidal_rule(f, a, b, 1)

#     for i in range(1, 5):  # Ahora el rango va desde 1 hasta 5
#         # Aproximaciones utilizando el método del trapecio con más subintervalos
#         R[i, 0] = 2**i
#         R[i, 1] = trapezoidal_rule(f, a, b, 2**i)

#         # Cálculo de Sn y Bn
#         if i > 0:
#             R[i, 2] = (4 * R[i, 1] - R[i - 1, 1]) / 3
#         if i > 1:
#             R[i, 3] = (16 * R[i, 2] - R[i - 1, 2]) / 15

#         # Construcción de la tabla con los datos
#         data = R[:i + 1, :]
#         table_headers = ["n", "Tn", "Sn", "Bn"]
#         print(tabulate(data, headers=table_headers, floatfmt=".10f"))
#         print("\n")

#         # Condición de convergencia
#         if abs(R[i, 2] - R[i, 1]) < tol:
#             break

#     return R[i, 2]

# # Calcular la aproximación del área bajo la curva y mostrar la tabla
# approx_area = romberg_integration_table(f, 0, 2)
# print("Aproximación del área usando el método de Romberg:", approx_area)
