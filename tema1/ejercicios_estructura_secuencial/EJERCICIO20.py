# Pedimos la cantidad de cada tipo de moneda
monedas_2 = int(input("¿Cuántas monedas de 2€ tienes? "))
monedas_1 = int(input("¿Cuántas monedas de 1€ tienes? "))
monedas_50 = int(input("¿Cuántas monedas de 50 céntimos tienes? "))
monedas_20 = int(input("¿Cuántas monedas de 20 céntimos tienes? "))
monedas_10 = int(input("¿Cuántas monedas de 10 céntimos tienes? "))

# Calculamos el total en euros
total = (monedas_2 * 2) + (monedas_1 * 1) + (monedas_50 * 0.50) + (monedas_20 * 0.20) + (monedas_10 * 0.10)

# Mostramos el resultado
print("El total que tienes es:", round(total, 2), "€")
