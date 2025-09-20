# Pedimos hora de salida
HH = int(input("Hora de salida (0-23): "))
MM = int(input("Minuto de salida (0-59): "))
SS = int(input("Segundo de salida (0-59): "))

# Tiempo de viaje en segundos
T = int(input("Duración del viaje en segundos: "))

# Convertimos hora de salida a segundos totales
salida_seg = HH * 3600 + MM * 60 + SS

# Hora de llegada en segundos
llegada_seg = salida_seg + T

# Convertimos a HH:MM:SS
HH_llegada = (llegada_seg // 3600) % 24   # %24 por si pasa de 24h
MM_llegada = (llegada_seg % 3600) // 60
SS_llegada = llegada_seg % 60

# Mostramos resultado
print(f"Hora de llegada: {HH_llegada:02d}:{MM_llegada:02d}:{SS_llegada:02d}")
