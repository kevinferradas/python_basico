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
                      






# Un objeto es la instancia de una clase.


# abstracción: no enfocarse en todas las propiedades, sino solamente en las que necesito.
# polimorfismo : podemos tener la misma función en diferentes signos
# encapsulamiento: