numero = int(input("Introduce un número de dos cifras: "))

if 10 <= abs(numero) <= 99:
    decenas = abs(numero) // 10
    unidades = abs(numero) % 10
    invertido = unidades * 10 + decenas

    # mantener el signo si el número era negativo
    if numero < 0:
        invertido = -invertido
    
    print("Número invertido:", invertido)
else:
    print("El número no es de dos cifras.")
