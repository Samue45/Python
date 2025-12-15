import json
import os
from Clases import Empleado, Gerente, Desarrollador

NOMBRE_ARCHIVO = "empleados.json"

lista_empleado = [
  {
    "tipo": "Gerente",
    "nombre": "Ana",
    "edad": 40,
    "departamento": "Ventas",
    "equipo": "Equipo Norte"
  },
  {
    "tipo": "Desarrollador",
    "nombre": "Luis",
    "edad": 30,
    "departamento": "IT",
    "lenguaje_programacion": "Python"
  },
  {
    "tipo": "Empleado",
    "nombre": "Marta",
    "edad": 25,
    "departamento": "Recursos Humanos"
  }
]

def crear_archivo_json(datos):
    try:
        with open(NOMBRE_ARCHIVO,'w',encoding='utf-8') as f:
            json.dump(datos, f , indent=4)
        print(f"Archivo '{NOMBRE_ARCHIVO}' creado/actualizado con éxito")
    except Exception as e:
        print(f"Error al escribir en el archivo JSON : {e}")

def leer_y_crear_instancias(): 
    if not os.path.exists(NOMBRE_ARCHIVO):
        print(f"ERROR: El archivo '{NOMBRE_ARCHIVO}' no existe")
        return []
    try:
        with open(NOMBRE_ARCHIVO,'r', encoding='utf-8') as f:
            datos = json.load(f)
    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []
    
    lista_instancias = []
    for emp_data in datos:
        tipo = emp_data.get("tipo")
        nombre = emp_data.get("nombre")
        edad = emp_data.get("edad")
        departamento = emp_data.get("departamento")

        if(tipo == "Gerente"):
            instancia = Gerente(nombre, edad, departamento, emp_data.get("equipo"))
        elif(tipo == "Desarrollador"):
             instancia = Desarrollador(nombre, edad, departamento, emp_data.get("lenguaje_programacion"))
        elif tipo == "Empleado":
            instancia = Empleado(nombre, edad, departamento)
        else:
            print(f"ADVERTENCIA: Tipo de empleado desconocido: {tipo}")
            continue

        lista_instancias.append(instancia)

    return lista_instancias

# --- Ejecución del Sistema ---

print("\n\n=== SISTEMA DE GESTIÓN DE EMPLEADOS ===")

# 1º Creamos el archivo JSON
crear_archivo_json(lista_empleado)

# 2º Leemos el archivo JSON y creamos las instancias de POO
empleados_cargados =leer_y_crear_instancias()

print("\n--- Informes de Empleados ---")

# 3. Mostrar la información de cada empleado (Polimorfismo en acción)
for empleado in empleados_cargados:
    print(empleado.mostrar_informacion())
    print("----------------------------")


