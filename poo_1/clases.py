class Persona():
    """
    Propiedades de una persona
    
    """
   
    # MÉTODOS
    # Método de instancia
    def __init__(self, nombre, apellido, funcion):
        self.nombre = nombre
        self.apellido = apellido
        self.funcion = funcion 

    def __str__(self):
        return f"Nombre:{self.nombre}, apellido : {self.apellido}, funcion: {self.funcion}"
    

    
persona_1= Persona("Peter", "Parker", "alumno")
print(persona_1)
                      

import os
os.system ("cls")

class Perro:
    
    # Atributo de clase
    especie = "mamífero" # todos los perros son mamíferos

    # El método __init__ (constructor) es llamado al crear el objeto
    # El self es una variable que representa la instancia de la clase
    # y deberá estar siempre.
    def __init__(self, nombre, raza):
         
        print(f"Creando perro {nombre}, {raza}")
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
    
    def __str__(self):
        return f"El perro se llama {self.nombre} y es de raza {self.raza}"

    # métodos de instancia 
    def ladra(self):
        print("Guau")

    def camina(self,pasos):
        print(f"Caminando {pasos} pasos.")
       


mi_perro = Perro("Toby", "Bulldog") # Creando perro Toby, Bulldog
print(type(mi_perro)) # <class '__main__.Perro'>
print(mi_perro)
print(mi_perro.nombre) # Toby
print(mi_perro.raza)   # Bulldog

# Para acceder a un atributo de clase, no es necesario crear un objeto
print(Perro.especie) # mamífero
print(mi_perro.especie) # mamífero

mi_perro.ladra() # Guau
mi_perro.camina(10) # Caminando 10 pasos







# Un objeto es la instancia de una clase.


# abstracción: no enfocarse en todas las propiedades, sino solamente en las que necesito.
# polimorfismo : podemos tener la misma función en diferentes signos
# encapsulamiento: