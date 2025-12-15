class Empleado:
    def __init__(self, nombre, edad, departamento):
        self.nombre = nombre
        self.edad = edad
        self.departamento = departamento
    
    def mostrar_informacion(self):
        print(f"Empleado [ Nombre = {self.nombre}, Edad = {self.edad}, Departamento = {self.departamento}]")
        
class Gerente(Empleado):
    def __init__(self, nombre, edad, departamento, equipo):
        super().__init__(nombre, edad, departamento)
        self.equipo = equipo

    def mostrar_informacion(self):
        print(f"Empleado [ Nombre = {self.nombre}, Edad = {self.edad}, Departamento = {self.departamento}, Equipo = {self.equipo}]")

class Desarrollador(Empleado):
    def __init__(self, nombre, edad, departamento, lenguaje_programacion):
        super().__init__(nombre, edad, departamento)
        self.lenguaje_programacion = lenguaje_programacion

    def mostrar_informacion(self):
        print(f"Empleado [ Nombre = {self.nombre}, Edad = {self.edad},"
              f"Departamento = {self.departamento}, Lenguaje de programacion = {self.lenguaje_programacion}]")
   