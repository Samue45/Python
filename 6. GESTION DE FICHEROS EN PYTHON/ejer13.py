import csv

NOMBRE_ARCHIVO = "productos.csv"

producto_user = input("Ingresa el nombre de un producto: ")

with open(NOMBRE_ARCHIVO,'r', encoding='utf-8') as f:
    lector = csv.DictReader(f)

    for producto in lector:
        if(producto.get("Nombre") == producto_user):
            print(f"El producto { producto.get("Nombre")} cuesta {producto.get("Precio")} €")
            break
        else:
            print(f"El producto {producto_user} no existe")
            break