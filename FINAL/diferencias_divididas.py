'''
Usar los siguientes tiempos (medidos en segundos) y posiciones (medidas en pies) para predecir 
la velocidad de un automovil en usando t=0 usando 3 puntos.
Tiempos(s): t0 = 0, t1 = 3, t2 = 5, t3 = 8, t4 = 10, t5 = 13
Distancia(pies): 0, 225, 383, 623, 742, 993
'''

tiempos = [0, 3, 5, 8, 10, 13]
distancias = [0, 225, 383, 623, 742, 993]


def diferencias_divididas(tiempos, distancias):
    n = len(tiempos)
    diferencias = [list(distancias)]

    for i in range(1, n):
        diff = []
        for j in range(n - i):
            numerador = diferencias[i - 1][j + 1] - diferencias[i - 1][j]
            denominador = tiempos[j + i] - tiempos[j]
            diff.append(numerador / denominador)
        diferencias.append(diff)

    return diferencias


def interpolacion_newton(t, tiempos, diferencias):
    n = len(tiempos)
    resultado = diferencias[0][0]
    multiplicador = 1

    for i in range(1, n):
        multiplicador *= (t - tiempos[i - 1])
        resultado += diferencias[i][0] * multiplicador

    return resultado


diferencias = diferencias_divididas(tiempos, distancias)


t = 0
velocidad = interpolacion_newton(t, tiempos, diferencias)
print(f"La velocidad en t = 0 es aproximadamente: {velocidad} pies/segundo") # Rpta: 0.0 pies/segundo