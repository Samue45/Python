import random

print(f"El lado ha sido lanzado y su resultado es {random.randint(1,12)}")

listaRandom = []

for i in range(100):
    listaRandom.append(random.randint(1,100))

print(listaRandom)