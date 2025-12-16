import json
import csv

with open("estudiante.json", 'r') as f_json:
    lista_estudiantes  = json.load(f_json)

with open("datos_convetidos.csv", 'w',newline='') as f_csv:
    if lista_estudiantes:
        campos = lista_estudiantes[0].keys()
        escritor = csv.DictWriter(f_csv, fieldnames= campos)
        escritor.writeheader()
        escritor.writerows(lista_estudiantes)
print("Archivo CSV creado con éxito")