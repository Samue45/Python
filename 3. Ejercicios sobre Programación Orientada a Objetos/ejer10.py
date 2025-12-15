import json

diccionario = {
    'nombre': 'Juan', 
    'edad': 30,
    'ciudad': 'Madrid',
}

json_str = json.dumps(diccionario)

print(f"Código a JSON = {json_str}")

codigo = json.loads(json_str)

print(f"JSON a código= {codigo}")