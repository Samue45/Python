import math

numberUser = int(input("Ingresa un número = "))
radioUser = int(input("Ingresa el radio de una circunferencia = "))

print(f"La raíz cuadrada del número {numberUser} es {math.sqrt(numberUser)}")
print(f"El área de la circunferencia cuyo radio es {radioUser} es {math.pi*(radioUser*radioUser)}")
