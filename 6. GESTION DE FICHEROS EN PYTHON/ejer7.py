
palabra_user = input("Ingresa una palabra: ")

with open("texto.txt",'r') as fr:
    lista_limpia_palabras = fr.read().split()
    contador = 0

    for letter in lista_limpia_palabras:
        if letter == palabra_user.strip():
            contador+=1
    if contador == 0:
        print("La palabra no existe")
    else:
        print(f"Tu palabra aparece {contador} veces")