import csv

datos = [
    {"Nombre": "Ana","Edad" : 20, "Curso": "Matemáticas"},
    {"Nombre": "Paco","Edad" : 30, "Curso": "Lengua"},
    {"Nombre": "Manu","Edad" : 20, "Curso": "Matemáticas"}
]

header = ["Nombre", "Edad", "Curso"]

with open("estudiante.csv",'w', newline='',encoding='utf-8') as f:
    escritor = csv.DictWriter(f ,fieldnames=header)

    escritor.writeheader()
    escritor.writerows(datos)
