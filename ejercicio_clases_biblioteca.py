"""
Programación Orientada a Objetos: Biblioteca

El programa debe crear las siguientes clases con sus métodos:

    Clase Lector, que se construirá con nombre y apellido

    Clase Libro, que se construirá con nombre_autor, apellido_autor,
    y título

    Clase Biblioteca, que se construirá con nombre y dirección
    Esta clase dispondrá de los siguientes métodos:
    - agregar_lector: agrega un lector a la biblioteca
    - mostrar lectores
    - agregar_libro: agrega un libro a la biblioteca,
        indicando los ejemplare disponibles
    - buscar_libro: busca un libro en la biblioteca, 
        indicando si lo tiene o no
    - mostrar libros de la biblioteca

"""
import os
os.system ("cls")

class Lector:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Libro :
    def __init__(self,nombre_autor,apellido_autor,titulo):
        self.nombre_autor = nombre_autor
        self.apellido_autor = apellido_autor
        self.titulo = titulo
        

class Biblioteca:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        # Atributos adicional para controlar la cantidad de lectores de la biblioteca
        self.lista_lectores=[]
        # Atributos adicional para controlar la cantidad de libros de la biblioteca.
        self.dic_libros={}
        # Atributos adicional para controlar la reserva de libros de la biblioteca.
        self.dic_reserva={}

    # Método para agregar lectores a la lista de lectores de la biblioteca
    # lector será una instancia de la clase Lector.
    def agregar_lector (self, lector):

        lector_datos = lector.nombre + " " +  lector.apellido
        # registro de nuevos usuarios
        if lector_datos not in self.lista_lectores:

            self.lista_lectores.append(lector_datos) # agregamos a un nuevo lector
            return f"Se ha añadido correctamente al usuario {lector.nombre} {lector.apellido}.\n"
        
        # si el usuario ya ha sido registrado antes...
        else:
            mensaje= f"El usuario {lector.nombre} {lector.apellido} ya ha sido registrado anteriormente."\
                     " Intente con otro nombre y apellido.\n"
            return mensaje 

    
    # Método para mostrar todos los lectores de la biblioteca
    def mostrar_lectores (self):
        mensaje=f"Los usuarios de la biblioteca {self.nombre}, son :\n"
        for lectores in self.lista_lectores:
            mensaje += f"- {lectores}\n\n"
        return mensaje

    # Método para agregar libros a la lista de libros de la biblioteca
    # libro será una instancia de la clase Libro
    # Se tendrá que especificar la cantidad de ejemplares de cierto libro.
    def agregar_libro(self,libro,ejemplares):
        
        # Registramos el libro por primera vez en el repositorio  
        if libro.titulo not in self.dic_libros:
            self.dic_libros [libro.titulo] = ejemplares #se añade un par libro:ejemplar en el diccionario.
            mensaje = f"Se han añadido {ejemplares} ejemplares del libro '{libro.titulo}'"\
                      f"del autor {libro.nombre_autor} {libro.apellido_autor}.\n"
            return mensaje

        # Agregamos ejemplares adicionales a un libro ya registrado.
        else:
            self.dic_libros [libro.titulo] += ejemplares # se suma una cant. adicional de ejemplares a un libro.
            mensaje = f"Se han añadido {ejemplares} ejemplares adicionales del libro '{libro.titulo}'"\
                      f"del autor {libro.nombre_autor} {libro.apellido_autor}.\n"
            return mensaje

    
    # Método para buscar un libro en el repositorio de la biblioteca (diccionario)
    # libro será una instancia de la clase Libro
    def buscar_libro (self,libro):

            if libro.titulo in self.dic_libros:
                return f"Disponemos de {self.dic_libros[libro.titulo]} ejemplares del libro '{libro.titulo}'.\n "
            else:
                return f"No disponemos del libro '{libro.titulo}' del autor {libro.nombre_autor} {libro.apellido_autor}.\n"

    # Método para mostrar todos los libros del repositorio.    
    def mostrar_libros (self):

        mensaje=f"La biblioteca {self.nombre} cuenta con los siguientes libros :\n"
        for libros in self.dic_libros:
            mensaje += f"- {libros} --> {self.dic_libros[libros]} ejemplares\n"
        return mensaje

    # Método para reservar un libro de la biblioteca.
    def reservar_libro (self,libro):
        
        if libro.titulo in self.dic_libros:
            self.dic_reserva [libro.titulo] = self.dic_libros[libro.titulo]
            return self.dic_reserva
        else:
            return f"No disponemos del libro '{libro.titulo}' del autor {libro.nombre_autor} {libro.apellido_autor}.\n"


# Creamos instancias de la clase Lector
anna = Lector ("Anna","Juarez")
kevin = Lector ("Kevin", "Ferradas") 
renato = Lector ("Renato", "González") 

# Creamos instancias de la clase Libro
libro = Libro("Gabriel", "Garcia","El amor en los tiempos del colera")
libro2= Libro("José","Saramago","Todos los nombre")
libro3= Libro ("Julio", "Cortázar", "Bestiario")
libro4= Libro ("George", "Orwell", "Rebelíón en la Granja")


# Creamos instancias de la clase Biblioteca
Bib_Agusti_Centelles = Biblioteca("Agusti Centelles","Eixample")

# Agregamos lectores a la biblioteca
print(Bib_Agusti_Centelles.agregar_lector(anna))
print(Bib_Agusti_Centelles.agregar_lector(kevin))
print(Bib_Agusti_Centelles.agregar_lector(renato))
print(Bib_Agusti_Centelles.agregar_lector(anna))


# mostramos los usuarios registrados en la biblioteca
print(Bib_Agusti_Centelles.mostrar_lectores())

# Agregamos libros al repositorio de la biblioteca
print(Bib_Agusti_Centelles.agregar_libro(libro,3))
print(Bib_Agusti_Centelles.agregar_libro(libro2,2))
print(Bib_Agusti_Centelles.agregar_libro(libro3,4))

# Agregamos más ejemplares a un libro ya registrado.
print(Bib_Agusti_Centelles.agregar_libro(libro,2))

# Buscamos libros (registrados) en el repositorio
print(Bib_Agusti_Centelles.buscar_libro(libro))

# Buscamos libros (no registrados) en el repositorio
print(Bib_Agusti_Centelles.buscar_libro(libro4))

# Mostramos los libros registrados en el repositorio 
print(Bib_Agusti_Centelles.mostrar_libros())
    
# Reservamos un libro del repositorio
print(Bib_Agusti_Centelles.reservar_libro(libro))