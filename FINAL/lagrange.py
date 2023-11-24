'''
Sean los puntos (1, 9), (3, -2) y (8, -5) al aplicar Lagrange:
p(x) = ((x-1)(x-3)/(8-1)(8-3))(a+c) + ((x-3)(x-8)/(1-3)(1-8))(a+b) + ((x-1)(x-8)/(3-1)(3-8))(c+b)
Calcule el valor de c.
'''

from sympy import symbols, simplify

x_vals = [1, 3, 8]
y_vals = [9, -2, -5]

x = symbols('x')

# Definir los términos de la fórmula de Lagrange
term_1 = ((x - x_vals[1]) * (x - x_vals[2])) / \
    ((x_vals[0] - x_vals[1]) * (x_vals[0] - x_vals[2])) * y_vals[0]
term_2 = ((x - x_vals[0]) * (x - x_vals[2])) / \
    ((x_vals[1] - x_vals[0]) * (x_vals[1] - x_vals[2])) * y_vals[1]
term_3 = ((x - x_vals[0]) * (x - x_vals[1])) / \
    ((x_vals[2] - x_vals[0]) * (x_vals[2] - x_vals[1])) * y_vals[2]

# Calcular el polinomio interpolante
pol_interpolante = term_1 + term_2 + term_3

# Simplificar el polinomio interpolante
pol_interpolante_simplificado = simplify(pol_interpolante)

# Mostrar el polinomio interpolante
print(f"El polinomio interpolante es: {pol_interpolante_simplificado}")

# Obtener los coeficientes del polinomio interpolante
coeficientes = pol_interpolante_simplificado.as_poly().all_coeffs()

# El coeficiente c corresponde al coeficiente de x^2
c = coeficientes[2]
print(f"El valor de c en el polinomio interpolante es: {c}")