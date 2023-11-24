from scipy import integrate

'''
Aproximar con el método de Simpson 1/3 la siguiente integral:
Integral de 1 a 2 de ((2x+1)/(x^2+x))dx 
Con h = 0.1 calcular el error cometido (7 decimates).
'''


def f(x):
    return (2 * x + 1) / (x**2 + x)


def simpson_13(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 4 * f(a + i * h)

    result *= h / 3
    return result


# Limite inferior
a = 1
# Limite superior
b = 2
# Tamaño de paso
h = 0.1

# Calcular la integral utilizando Simpson 1/3
n = int((b - a) / h)
approx_integral = simpson_13(f, a, b, n)

# Calcular el valor exacto de la integral utilizando scipy.integrate.quad
exact_integral, _ = integrate.quad(f, a, b)
error = abs(exact_integral - approx_integral)

print(f"Aproximación de la integral usando Simpson 1/3: {approx_integral}")
print(f"Valor exacto de la integral: {exact_integral}")
print(f"Error cometido: {error:.7f}")