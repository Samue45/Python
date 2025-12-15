# Creación de la clase Libro
class Libro:
    def __init__(self,titulo,autor,anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def print_description(self):
        print(f"'{self.titulo}' fue escrito por {self.autor} en el año {self.anio_publicacion}.")

# Creación de los objetos y uso del método
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)

libro1.print_description()
libro2.print_description()
