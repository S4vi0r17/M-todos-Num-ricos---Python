import math

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

# Función a derivar
def example_function(x):
    return math.exp(- x ** 2)

x = 1.0  # Punto para la derivada
step_sizes = [0.1, 0.05, 0.01]  # Pasos

for h in step_sizes:
    backward_derivative = backward_difference(example_function, x, h)
    central_derivative = central_difference(example_function, x, h)
    forward_derivative = forward_difference(example_function, x, h)

    print(f"Tamaño de paso h = {h}:")
    print(f"Derivada hacia atrás: {backward_derivative}")
    print(f"Derivada centrada: {central_derivative}")
    print(f"Derivada hacia adelante: {forward_derivative}")
    print()
