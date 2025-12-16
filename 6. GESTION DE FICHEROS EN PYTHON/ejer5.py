NOMBRE_ARCHIVO = "texto.txt"

try:
    with open(NOMBRE_ARCHIVO,'w') as fw:
        fw.write("Soy una línea de texto")
    
    with open(NOMBRE_ARCHIVO,'r') as fr:
        texto_limpio = fr.read().split()
        contador = len(texto_limpio)
        print(f"En total hay {contador} palabras")
except IOError as e:
    print(e)
        
