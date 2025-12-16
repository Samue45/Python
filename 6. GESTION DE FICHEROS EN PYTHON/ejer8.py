import os

NOMBRE_ARCHIVO1 = "datos.txt"
NOMBRE_ARCHIVO2 = "texto.txt"

datos = "Nombre : Juan Pérez \nEdad : 30 \nCiudad : Madrid \nProfesión : Arquitecto"

with open(NOMBRE_ARCHIVO1,'w') as fw:
    fw.write(datos)

with open(NOMBRE_ARCHIVO1,'r') as fr:
    contenido = fr.read()
    print(contenido)

with open(NOMBRE_ARCHIVO1,'r') as fr:
    contenido = fr.read().strip().split()
    print(contenido)

with open(NOMBRE_ARCHIVO1,'a') as fa:
    fa.write("Situación laboral : Parado")


with open(NOMBRE_ARCHIVO2,'r') as fr:
    lista_palabras_limpia = fr.read().strip().split()
    contador = len(lista_palabras_limpia)
    print(f"Total de palabras = { contador}")

with open("temp_file.dat",'w') as fw:
    fw.write("hola")

os.rename("temp_file.dat", "registro_proceso.dat")
os.mkdir("archivos_log")
print(os.listdir("."))

os.remove("registro_proceso.dat")
os.rmdir("archivos_log")