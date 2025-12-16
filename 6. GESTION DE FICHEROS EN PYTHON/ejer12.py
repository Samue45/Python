import csv

NOMBRE_ARCHIVO = "productos.csv"


with open(NOMBRE_ARCHIVO,'r', encoding='utf-8') as f:
    lector = csv.reader(f)
    next(lector)

    contador = 0

    for producto in lector:
        contador += 1
    
    print(f"Hay {contador} productos")