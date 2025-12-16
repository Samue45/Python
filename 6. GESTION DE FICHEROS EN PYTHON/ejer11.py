import csv

NOMBRE_ARCHIVO = "productos.csv"

with open(NOMBRE_ARCHIVO,'r',encoding="utf-8") as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)

