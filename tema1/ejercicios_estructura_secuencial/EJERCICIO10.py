# Pedimos las notas al usuario
nota1 = float(input("Introduce la primera nota parcial: "))
nota2 = float(input("Introduce la segunda nota parcial: "))
nota3 = float(input("Introduce la tercera nota parcial: "))

examen_final = float(input("Introduce la nota del examen final: "))
trabajo_final = float(input("Introduce la nota del trabajo final: "))

# Calculamos el promedio de las parciales
promedio_parciales = (nota1 + nota2 + nota3) / 3

# Calculamos la nota final con los porcentajes
nota_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
# Mostramos el resultado
print("La calificación final en Algoritmos es:", round(nota_final, 2))
