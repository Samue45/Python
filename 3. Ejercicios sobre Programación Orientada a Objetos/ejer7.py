import os

nombre_carpeta = "Carpeta 1"

os.mkdir(nombre_carpeta)

print(f"Nueva carpeta creada con nombre  {nombre_carpeta}")

contenido = os.listdir('.')

for file in contenido:
    print(f"Archivo {file}")