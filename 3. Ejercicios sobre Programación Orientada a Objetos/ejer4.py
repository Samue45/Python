class Vehiculo:
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def informacion(self):
        print(f"Vehículo [marca = {self.marca}, modelo = {self.modelo}, color = {self.color}]")
    

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, numero_puertas):
        super().__init__(marca, modelo, color)
        self.numeros_puertas = numero_puertas
    
    def informacion(self):
        print(f"Coche [marca = {self.marca}, modelo = {self.modelo}, color = {self.color}, numeros_puertas = {self.numeros_puertas}]")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, color, numero_ruedas):
        super().__init__(marca, modelo, color)
        self.numero_ruedas = numero_ruedas
    
    def informacion(self):
        print(f"Coche [marca = {self.marca}, modelo = {self.modelo}, color = {self.color}, numeros_ruedas = {self.numero_ruedas}]")

    
coche1 = Coche("Audi", "123", "blanco", 4)
motocicleta = Motocicleta("Moto", "123", "blanco", 2)

coche1.informacion()
motocicleta.informacion()