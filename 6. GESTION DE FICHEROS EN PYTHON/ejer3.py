NOMBRE_ARCHIVO="datos.txt"

try:
    with open(NOMBRE_ARCHIVO,'r') as f:

        for linea in f:
            linea_limpia = linea.split()
            print(linea_limpia)
except FileNotFoundError as e:
    print(f"Error {e}")


