import sympy as sp

# Define la variable simbólica
x = sp.Symbol('x')
# (x + √x)((20 - x) + √(20 - x)) = 155.55
f = (x + sp.sqrt(x)) * ((20 - x) + sp.sqrt(20 - x)) - 155.55
# f = x**2 * sp.pi * (9-x) -60

# Calcula automáticamente la derivada de la función
f_derivada = sp.diff(f, x)

print("\nx0\t\tf(x0)\t\tf'(x0)\t\tx1\t\tE(error relativo)")


def newton_raphson(f, x0, tol):
    while True:
        f_value = f.subs(x, x0).evalf()
        f_derivada_value = f_derivada.subs(x, x0).evalf()

        x1 = x0 - f_value / f_derivada_value

        error = abs(x1 - x0) / abs(x1)

        # Mostrar la información de la iteración
        print(f"{x0:.10f}\t{f_value:.12f}\t{f_derivada_value:.10f}\t{x1:.10f}\t{error:.10f} => {error:.10e}")

        if error < tol:
            return x1

        x0 = x1


# Uso del método de Newton-Raphson
x0 = 1
tolerance = 1e-3
root = newton_raphson(f, x0, tolerance)

print("El valor de x es ~ ", root)
print("El valor de y es ~ ", 20-root)
