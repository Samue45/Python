contenido_copiado=""

with open("datos.txt", 'r') as fr:
    with open("copia.txt", 'w') as fw:
        contenido_copiado = fr.read()
        fw.write(contenido_copiado)
        print(contenido_copiado)