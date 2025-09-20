# Pedimos los datos
d = float(input("Introduce la distancia entre los vehículos (km): "))
v1 = float(input("Introduce la velocidad del vehículo de delante (km/h): "))
v2 = float(input("Introduce la velocidad del vehículo de detrás (km/h): "))

# Calculamos el tiempo en horas
tiempo_horas = d / (v2 - v1)

# Convertimos a minutos
tiempo_minutos = tiempo_horas * 60

# Mostramos resultado
print(f"El vehículo más rápido alcanzará al otro en: {tiempo_minutos:.2f} minutos")
