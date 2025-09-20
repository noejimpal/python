# Ejercicio 8: Sueldo con comisiones

# Entrada de datos
sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
venta1 = float(input("Ingrese el valor de la primera venta: "))
venta2 = float(input("Ingrese el valor de la segunda venta: "))
venta3 = float(input("Ingrese el valor de la tercera venta: "))

# Cálculo de la comisión (10% del total de las ventas)
comision = 0.10 * (venta1 + venta2 + venta3)

# Cálculo del total a recibir
total = sueldo_base + comision

# Salida de resultados

print("Comisión total: $", comision)
print("Total a recibir en el mes: $", total)
