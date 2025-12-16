NOMBRE_ARCHIVO="datos.txt"

try:
    with open(NOMBRE_ARCHIVO, 'a') as f:
        f.write("Profesión: Ingeniero")
except FileNotFoundError as e:
    print(e)