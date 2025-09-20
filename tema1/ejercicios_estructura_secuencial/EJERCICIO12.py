import math  # Para usar sqrt (raíz cuadrada)

# Pedir las coordenadas de los dos puntos
x1 = float(input("Introduce x1: "))
y1 = float(input("Introduce y1: "))
x2 = float(input("Introduce x2: "))
y2 = float(input("Introduce y2: "))

# Calcular la distancia con la fórmula
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mostrar el resultado
print("La distancia entre los dos puntos es:", distancia)
