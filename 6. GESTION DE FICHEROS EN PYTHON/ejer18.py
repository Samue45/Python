import json

tarea_user = input("Ingresa tu tarea : ")
tareas = []

with open("tareas.json", 'r' , encoding='utf-8') as fr:
    datos = json.load(fr)
    tareas = datos.get("tareas")
    tareas.append(tarea_user)

with open("tareas.json", 'w' , encoding='utf-8') as fr:
    json.dump({"tareas": tareas}, fr, indent= 4)
    print("Tarea agregada correctamente.")




