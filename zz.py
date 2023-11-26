# Datos proporcionados en minutos
gasto_petroleo = [20.4, 22.1, 18.7, 23.4, 26.7, 21.4, 19.8, 21.9, 22.3]
tiempo_minutos = [0, 180, 360, 540, 720, 900, 1080, 1260, 1440]  # Convertido a minutos

# Calculando el tamaño del intervalo en minutos
h = tiempo_minutos[1] - tiempo_minutos[0]
print("Tamaño del intervalo (h):", h, "minutos")

# Calculando t0 y tn en minutos
t0 = tiempo_minutos[0]
tn = tiempo_minutos[-1]
print("t0 (tiempo inicial):", t0, "minutos")
print("tn (tiempo final):", tn, "minutos")

# Calculando las sumas de los puntos impares y pares
sum_impares = sum(gasto_petroleo[1:-1:2])  # Suma de los puntos impares
sum_pares = sum(gasto_petroleo[2:-1:2])    # Suma de los puntos pares

print("Suma de los puntos impares:", sum_impares)
print("Suma de los puntos pares:", sum_pares)

# Aplicando la fórmula de Simpson para aproximar la cantidad de petróleo gastado en 24 horas
cantidad_petroleo_24h_simpson = (h / 3) * (gasto_petroleo[0] + 4 * sum_impares + 2 * sum_pares + gasto_petroleo[-1])
print("a) Cantidad de petróleo gastado en 24 horas (Regla de Simpson):", cantidad_petroleo_24h_simpson, "Kg")

# Calculando el gasto promedio de petróleo en minutos
gasto_promedio = sum(gasto_petroleo) / len(gasto_petroleo)
print("c) Gasto promedio de petróleo:", gasto_promedio, "Kg/min")


# Calculando el gasto promedio de petróleo en minutos
gasto_promedio = sum(gasto_petroleo) / len(gasto_petroleo)
print("c) Gasto promedio de petróleo:", gasto_promedio, "Kg/min")
