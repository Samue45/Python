import csv
import json

ARCHIVO_CSV="estudiante.csv"
ARCHIVO_JSON="estudiante.json"

# 1 Cargamos los datos del archivo csv
with open(ARCHIVO_CSV,'r') as f:
    lector = csv.DictReader(f)
    lista_estudiantes = list(lector)

# 2º Creamos el archivo JSON con los datos cargados
with open(ARCHIVO_JSON,'w') as fr:
    json.dump(lista_estudiantes, fr, indent=4)
    print("Archivo json creado")