# Pedir nombre y apellidos
nombre = input("Introduce tu nombre: ")
apellido1 = input("Introduce tu primer apellido: ")
apellido2 = input("Introduce tu segundo apellido: ")

# Obtener iniciales (primer carácter de cada uno)
iniciales = nombre[0].upper() + apellido1[0].upper() + apellido2[0].upper()

# Mostrar el resultado
print("Tus iniciales son:", iniciales)
