import json

nombre_user = input("Ingresa tu nombre : ")
edad_user = int(input("Ingresa tu edad : "))
ciudad_user = input("Ingresa tu ciudad : ")

datos = { "nombre": nombre_user, "edad" : edad_user, "ciudad": ciudad_user}

with open("usuario.json", 'w', encoding= 'utf-8') as f:
    json.dump(datos, f, indent=4)


