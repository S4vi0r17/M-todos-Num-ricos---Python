def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Ejemplo de uso
def ejemplo_funcion(x):
    return x**3 - x + 2

x0 = 2.0  # Punto en el que deseas calcular la derivada
h = 0.001  # Pequeño incremento

derivada_forward = forward_difference(ejemplo_funcion, x0, h)
derivada_backward = backward_difference(ejemplo_funcion, x0, h)
derivada_central = central_difference(ejemplo_funcion, x0, h)

print(f'Derivada hacia adelante: {derivada_forward}')
print(f'Derivada hacia atrás: {derivada_backward}')
print(f'Derivada central: {derivada_central}')
