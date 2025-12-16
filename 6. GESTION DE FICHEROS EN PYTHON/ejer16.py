import json

persona1 = {"nombre" : "Luis", "edad": 20, "ciudad":"Jerez"}
persona2 = {"nombre" : "Paco", "edad": 40, "ciudad":"Madrid"}

with open("datos.json",'w',encoding='utf-8') as f:
    json.dump(persona1, f, indent=4)

with open("datos.json", 'r', encoding='utf-8') as f:
    datos_cargados = json.load(f)
    print(datos_cargados)
