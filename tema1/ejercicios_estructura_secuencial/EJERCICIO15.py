A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))

print("Antes del intercambio -> A:", A, " B:", B)

A = A + B
B = A - B
A = A - B

print("Después del intercambio -> A:", A, " B:", B)

