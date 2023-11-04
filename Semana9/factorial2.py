# Importar librería numpy
import numpy as np

# Definir los datos de entrada
xi = np.array([0, 1, 2, 3]) # Puntos dados en x
yi = np.array([2, 1.3679, 1.1353, 1.0497]) # Puntos dados en y
n = len(xi) # Número de puntos

# Calcular las diferencias divididas
dd = np.zeros((n, n)) # Matriz vacía para almacenar las diferencias
dd[:, 0] = yi # La primera columna es igual a los valores de y
for j in range(1, n): # Iterar sobre las columnas
  for i in range(n-j): # Iterar sobre las filas
    dd[i, j] = (dd[i+1, j-1] - dd[i, j-1]) / (xi[i+j] - xi[i]) # Aplicar la fórmula recursiva

# Imprimir la tabla con formato
print("Tabla de diferencias divididas:")
print("xi\t\t yi\t\t Δ\t\t Δ^2\t\t Δ^3") # Imprimir los encabezados
for i in range(n): # Iterar sobre las filas
  print(f"{xi[i]:.1f}\t\t", end="") # Imprimir el valor de x con un tabulador
  for j in range(n-i): # Iterar sobre las columnas
    print(f"{dd[i, j]:.4f}\t\t", end="") # Imprimir el valor de la diferencia con un tabulador
  print() # Salto de línea
