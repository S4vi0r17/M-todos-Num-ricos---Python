'''
Calcule el valor de E(1.3)
El voltaje de un circuito eléctrico satisface la ecuaci6n E(t) = L((dI(t))/(dt))+ R I(t), donde R es la resistencia, L es la inductancia e I(t) es la intensidad de corriente. 
Considere L = 0.04 henrios, R = 2.5 ohmios y los valores de la intensidad I(t) en amperios, que se relacionan en la siguiente tabla.
I(t): 8.1234, 7.7651, 6.3425, 4.8793
t: 1.0, 1.2, 1.4, 1.6
'''

import scipy.interpolate

x = [1.0, 1.2, 1.4, 1.6]
y = [8.1234, 7.7651, 6.3425, 4.8793]

# Crear la función de interpolación lineal
y_interp = scipy.interpolate.interp1d(x, y)

# Hallar el valor de I(1.3) usando la función de interpolación
I_13 = y_interp(1.3)
print("El valor de I(1.3) es: %0.4f" % (I_13))

# Hallar el valor de la derivada (dI/dt)(1.3) usando la pendiente de la recta
dIdt_13 = (y_interp(1.4) - y_interp(1.2)) / (1.4 - 1.2)
print("El valor de (dI/dt)(1.3) es: %0.4f" % (dIdt_13))

# Definir los valores de L y R dados en el ejercicio
L = 0.04
R = 2.5

# Hallar el valor de E(1.3) usando la ecuación del voltaje
E_13 = L * dIdt_13 + R * I_13
print("El valor de E(1.3) es: %0.4f" % (E_13))

# El valor de I(1.3) es: 7.0538
# El valor de (dI/dt)(1.3) es: -7.1130
# El valor de E(1.3) es: 17.3500