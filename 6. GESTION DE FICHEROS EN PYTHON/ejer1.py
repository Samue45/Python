NOMBRE_ARCHIVO="datos.txt"

try:
    with open(NOMBRE_ARCHIVO,'w') as f:
        f.write("Nombre: Juan\n")
        f.write("Edad: 80\n")
        f.write("Ciudad: Madrid\n")
except IOError as e:
    print(f"Error = {e}")
