import sympy as sp

# Define la variable simbólica
x = sp.Symbol('x')

# Define la función
f = sp.exp(-x) - x

# Calcula automáticamente la derivada de la función
f_derivada = sp.diff(f, x)

print("\nx0\t\tf(x0)\t\tf'(x0)\t\tx1\t\tE(error relativo)")

def newton_raphson(f, x0, tol):

    while True:
        f_value = f.subs(x, x0) # x es la variable simbólica y x0 es el valor numérico
        f_derivada_value = f_derivada.subs(x, x0)
        
        x1 = x0 - f_value / f_derivada_value
        
        error = abs(x1 - x0) / abs(x1)

        # Mostrar la información de la iteración
        print(f"{x0:.10f}\t{f_value:.12f}\t{f_derivada_value:.10f}\t{x1:.10f}\t{error:.10f} => {error:.10e}")
        
        
        if error < tol:
            return x1
        
        x0 = x1


# Uso del método de Newton-Raphson
x0 = 0.5
tolerance = 1e-3
root = newton_raphson(f, x0, tolerance)

print("La raíz aproximada es:", root)
