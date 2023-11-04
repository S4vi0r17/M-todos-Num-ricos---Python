# Datos proporcionados
n = 3  # Orden del polinomio
s = 0.2  # Valor de s
y0 = 2  # Valor de y0
delta_y0 = 1.3679 - y0  # Δ y0
delta2_y0 = 1.1353 - (1.3679)  # Δ^2 y0
delta3_y0 = 1.0497 - 1.1353  # Δ^3 y0

# Calcular el valor de p(0.2) utilizando la fórmula
p_0_2 = y0 + (delta_y0 * s) / 1 + (delta2_y0 * (s**2)) / 2 + (delta3_y0 * (s**3)) / 6

# Imprimir la fórmula y su valor
formula = f"p(x) = {y0} + ({delta_y0} * s) / 1 + ({delta2_y0} * (s**2)) / 2 + ({delta3_y0} * (s**3)) / 6"
print("Fórmula:")
print(formula)
print(f"\np(0.2) = {p_0_2}")
# Importar librerías
import numpy as np
import matplotlib.pyplot as plt

# Definir función para calcular los coeficientes del polinomio de Newton
def coeficientes(x, y):
  n = len(x) # Número de puntos
  a = np.copy(y) # Arreglo para almacenar los coeficientes
  for k in range(1, n): # Iterar sobre las columnas de la matriz de diferencias divididas
    a[k:n] = (a[k:n] - a[k-1]) / (x[k:n] - x[k-1]) # Calcular las diferencias divididas
  return a # Devolver los coeficientes

# Definir función para evaluar el polinomio de Newton en un punto
def evaluar(a, x, z):
  n = len(a) - 1 # Grado del polinomio
  p = a[n] # Inicializar el valor del polinomio
  for k in range(1, n+1): # Iterar sobre los coeficientes
    p = a[n-k] + (z - x[n-k]) * p # Aplicar la fórmula recursiva del polinomio
  return p # Devolver el valor del polinomio

# Definir los datos de entrada
n = 3 # Grado del polinomio
x = np.array([0, 1, 2, 3]) # Puntos dados en x
y = np.array([2, 1.3679, 1.1353, 1.0497]) # Puntos dados en y
z = 0.2 # Punto a evaluar

# Llamar a las funciones y mostrar los resultados
a = coeficientes(x, y) # Calcular los coeficientes del polinomio
p = evaluar(a, x, z) # Evaluar el polinomio en el punto dado
print("El polinomio de interpolación de Newton es:")
print(f"p(x) = {a[0]:.4f}", end="") # Mostrar el primer coeficiente
for k in range(1, n+1): # Mostrar el resto de los coeficientes
  print(f" + {a[k]:.4f}", end="") # Mostrar el signo y el valor del coeficiente
  for i in range(k): # Mostrar los términos del polinomio
    print(f"(x - {x[i]:.1f})", end="") # Mostrar el signo y el valor del punto
print() # Salto de línea
print("Los valores de los términos del polinomio son:")
s = z - x[0] # Calcular el primer término
print(f"s^(1) = {s:.4f}") # Mostrar el primer término
for k in range(2, n+1): # Calcular el resto de los términos
  s = s * (z - x[k-1]) # Aplicar la fórmula recursiva del término
  print(f"s^({k}) = {s:.4f}") # Mostrar el término
print(f"El valor del polinomio en x = {z:.1f} es:")
print(f"p({z:.1f}) = {p:.4f}") # Mostrar el valor del polinomio
