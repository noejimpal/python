# Pedir datos al usuario
correctas = int(input("Introduce la cantidad de respuestas correctas: "))
incorrectas = int(input("Introduce la cantidad de respuestas incorrectas: "))
blanco = int(input("Introduce la cantidad de respuestas en blanco: "))

# Calcular nota
nota_final = (correctas * 5) + (incorrectas * -1) + (blanco * 0)

# Mostrar resultado
print("La nota final del estudiante es:", nota_final)
