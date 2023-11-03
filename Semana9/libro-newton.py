# Importar numpy para usar arrays
import numpy as np

# Definir los puntos dados
xi = np.array([50, 60, 70, 80, 90, 100])
fi = np.array([24.94, 30.11, 36.05, 42.84, 50.57, 59.30])

# Calcular el número de puntos
n = len(xi)

# Crear una matriz vacía para almacenar las diferencias divididas
dd = np.zeros((n, n))

# Llenar la primera columna con los valores de la función
dd[:, 0] = fi

# Calcular las diferencias divididas usando el método recursivo
for j in range(1, n):
    for i in range(n-j):
        dd[i, j] = (dd[i+1, j-1] - dd[i, j-1]) / (xi[i+j] - xi[i])

# Definir la función que evalúa el polinomio en un punto x
def newton(x):
    # Inicializar el valor del polinomio
    p = dd[0, 0]
    # Inicializar el producto de los términos (x-xi)
    prod = 1
    # Sumar los términos restantes del polinomio
    for k in range(1, n):
        prod = prod * (x - xi[k-1])
        p = p + dd[0, k] * prod
    # Devolver el valor del polinomio
    return p

# Interpolar la presión a la temperatura de 64°F
p64 = newton(64)

# Imprimir el resultado
print(f"La presión interpolada a 64°F es {p64:.2f} lb/plg2")

# Importar pandas para crear y mostrar la tabla
import pandas as pd

# Crear un dataframe con los datos de la tabla
df = pd.DataFrame(data=dd, index=xi, columns=["f[xi]", "Primera", "Segunda", "Tercera", "Cuarta", "Quinta"])

# Imprimir la tabla con formato
print(df.to_string(float_format="{:.4f}".format))
