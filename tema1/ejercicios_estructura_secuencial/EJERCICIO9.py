# Pedir el total de la compra
compra = float(input("Introduce el total de la compra: "))

# Calcular el descuento (15%)
descuento = compra * 0.15

# Calcular el precio final
pago_final = compra - descuento

# resultados
print("Descuento aplicado:", descuento)
print("El total a pagar es:", pago_final)
