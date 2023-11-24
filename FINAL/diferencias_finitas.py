'''
Dado los siguientes puntos:
x: 0, 2, 4
f(x): 3, 10, 15
Calcular la derivada en los puntos xO, x1 y x2 utilizando tres puntos. 
Dar como resultado la suma de las derivadas calculadas.
'''
x = [0, 2, 4]
f_x = [3, 10, 15]


def derivada_tres_puntos(x, f_x, i):
    # Si i es el primer índice de la lista, usar la diferencia finita hacia adelante
    if i == 0:
        return (f_x[i+1] - f_x[i]) / (x[i+1] - x[i])
    # Si i es el último índice de la lista, usar la diferencia finita hacia atrás
    elif i == len(x) - 1:
        return (f_x[i] - f_x[i-1]) / (x[i] - x[i-1])
    # Para otros índices, usar la diferencia finita centrada
    else:
        return (f_x[i+1] - f_x[i-1]) / (x[i+1] - x[i-1])


f_x0 = derivada_tres_puntos(x, f_x, 0)
f_x1 = derivada_tres_puntos(x, f_x, 1)
f_x2 = derivada_tres_puntos(x, f_x, 2)

print(f"La derivada en x0 es {f_x0}")
print(f"La derivada en x1 es {f_x1}")
print(f"La derivada en x2 es {f_x2}")

suma = f_x0 + f_x1 + f_x2

print(f"La suma de las derivadas es {suma}") # Rpta: 9.0