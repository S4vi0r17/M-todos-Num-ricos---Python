import numpy as np
import sympy as sp

# Define la variable simbólica
x = sp.symbols('x')

# Función a integrar (f(x))
def f(x_value):
    return np.exp(-x_value**2)

# Calcula las derivadas segunda y cuarta de la función simbólicamente
f_sym = sp.exp(-x**2)
f_second_deriv = sp.diff(f_sym, x, 2)
f_fourth_deriv = sp.diff(f_sym, x, 4)

# Convierte las expresiones simbólicas en funciones numéricas para evaluación
f_second_deriv_func = sp.lambdify(x, f_second_deriv, 'numpy')
f_fourth_deriv_func = sp.lambdify(x, f_fourth_deriv, 'numpy')

# Regla del trapecio para el cálculo de la integral
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Regla de Simpson compuesta para el cálculo de la integral
def simpson_composite(f, a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * f(a + i * h)
        else:
            integral += 4 * f(a + i * h)
    integral *= h / 3
    return integral

# Fórmulas proporcionadas por el profesor para los errores
def error_trapecio(h, f_deriv):
    return abs((-h**2 / 12) * f_deriv)

def error_simpson(h, f_deriv):
    return abs((-h**5 / 90) * f_deriv)

def error_trapecio_compuesto(n, h, f_deriv):
    return abs((-n * h**3 / 12) * f_deriv)

def error_simpson_compuesto(n, h, f_deriv):
    return abs((-n * h**5 / 180) * f_deriv)

# Límites de integración
a = 0
b = 2

# Número de nodos
nodos = 7

# Aproximación del volumen utilizando el método del trapecio y la regla de Simpson compuesta
volumen_trapecio = np.pi * trapezoidal_rule(f, a, b, nodos)
volumen_simpson = np.pi * simpson_composite(f, a, b, nodos)

# Tamaños de paso
h = (b - a) / nodos

# Errores utilizando las fórmulas proporcionadas por el profesor
error_et = error_trapecio(h, f_second_deriv_func(a))
error_es = error_simpson(h, f_fourth_deriv_func(a))
error_ect = error_trapecio_compuesto(nodos, h, f_second_deriv_func(a))
error_ecs = error_simpson_compuesto(nodos, h, f_fourth_deriv_func(a))

# Mostrar los resultados
print(f"Aproximación del volumen del sólido de revolución (Trapecio): {volumen_trapecio}")
print(f"Aproximación del volumen del sólido de revolución (Simpson): {volumen_simpson}")
print(f"Error estimado con la fórmula del método del trapecio: {error_et}")
print(f"Error estimado con la fórmula de la regla de Simpson: {error_es}")
print(f"Error estimado con la fórmula del método del trapecio compuesto: {error_ect}")
print(f"Error estimado con la fórmula de la regla de Simpson compuesta: {error_ecs}")
