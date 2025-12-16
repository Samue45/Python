# 📁 Gestión de ficheros en Python – Librerías y funciones útiles

En el contenido proporcionado se mencionan las siguientes **librerías (módulos), funciones y métodos** que ayudan en el proceso de gestión de ficheros y tratamiento de texto en Python.

---

## 1️⃣ `open()` (función integrada)

> ⚠️ **No es una librería**, es una función incorporada en Python.

- Permite abrir archivos para lectura, escritura, añadido, modo binario, etc.
- Es la base de la gestión de ficheros.

**Ejemplo:**
```python
archivo = open("archivo.txt", "r", encoding="utf-8")

import os

os.path.exists()	Comprueba si un archivo o directorio existe.	os.path.exists("datos.txt")
os.rename()	Renombra archivos o directorios.	os.rename("viejo.txt", "nuevo.txt")
os.remove()	Elimina archivos.	os.remove("obsoleto.txt")
os.mkdir()	Crea una carpeta (directorio).	os.mkdir("mi_carpeta")
os.listdir()	Lista los archivos y carpetas de un directorio.	os.listdir(".")

import shutil

shutil.copy(),Copia un archivo de una ubicación a otra.,"shutil.copy(""origen.txt"", ""destino.txt"")"
shutil.move(),Mueve (o renombra) un archivo o directorio.,"shutil.move(""fichero.txt"", ""carpeta/"")"
shutil.rmtree(),"Elimina carpetas con todo su contenido (peligroso, pero útil).","shutil.rmtree(""carpeta_llena"")"

import csv

csv.reader()	Leer filas de un CSV como listas (útil para archivos sencillos).
csv.writer()	Escribir listas en un CSV.
csv.DictReader()	Leer filas de un CSV como diccionarios (más fácil de manejar con encabezados).
csv.DictWriter()	Escribir diccionarios en un CSV.

import json

json.load()	Leer datos JSON desde un archivo.	—
json.dump()	Escribir datos Python en un archivo JSON.	—
json.loads()	Convertir una cadena JSON en objeto Python (diccionario/lista).	
json.dumps()	Convertir un objeto Python (diccionario/lista) en una cadena JSON.

strip() (Método de Cadenas)
Función: Elimina los espacios en blanco, tabulaciones y saltos de línea (\n) al inicio y al final de una cadena.

Ejemplo:

Python

linea = " Hola mundo \n"
print(linea.strip())  # Salida: "Hola mundo"
🔹 split() (Método de Cadenas)
Función: Divide una cadena en una lista de subcadenas (palabras).

Por Defecto: Si no se da argumento, usa cualquier espacio en blanco como separador.

Ejemplo sin separador:

Python

texto = "Python es muy potente"
palabras = texto.split()
print(palabras) # Salida: ['Python', 'es', 'muy', 'potente']
Ejemplo con separador personalizado:

Python

datos = "Ana,25,Madrid"
lista = datos.split(",")
print(lista) # Salida: ['Ana', '25', 'Madrid']
🔹 len() (Función Integrada)
Función: Cuenta la cantidad de elementos de un iterable (listas, cadenas, tuplas, diccionarios, etc.).

Uso Frecuente: Muy utilizada para contar palabras o líneas después de usar split().

Ejemplo:

Python

palabras = ["Hola", "Python"]
print(len(palabras))  # Salida: 2
Ejemplo práctico con archivos:

Python

contenido = "Hola mundo desde Python"
numero_palabras = len(contenido.split())
print(numero_palabras) # Salida: 4