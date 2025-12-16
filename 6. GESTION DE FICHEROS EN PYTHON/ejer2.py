NOMBRE_ARCHIVO="datos.txt"

contenido =""

try:
    with open(NOMBRE_ARCHIVO,'r') as f:
        contenido = f.read()
except FileNotFoundError:
    print("\n¡Error! El archivo 'datos.txt' no se encontró.")
    print("Asegúrate de haber ejecutado primero el Ejercicio 1 para crearlo.")
except IOError as e:
    print(f"\nOcurrió un error de E/S (Input/Output): {e}")

print(f"Contenido del archivo \n{contenido}")