import csv

nombre_user = input("Ingresa tu nombre : ")
edad_user = int(input("Ingresa tu edad : "))
curso_user = input("Ingresa tu curso : ")


with open("estudiante.csv", 'a',newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([nombre_user, edad_user, curso_user])
