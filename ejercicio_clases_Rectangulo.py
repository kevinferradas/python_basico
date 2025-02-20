"""
Hay que crear una clase llamada Rectangulo.

Necesitamos los métodos para obtener el área, el perímetro y la diagonal de la figura.

Cada uno en un método diferente.

Lo probaremos con un rectángulo de lados 3 y 4.
"""
import os
os.system ("cls")


# Definimos la clase Rectángulo
class Rectangulo ():
    
    def __init__(self, largo: int, ancho: int):
        self.largo = largo
        self.ancho = ancho 


    # def __str__(self):
    #     print( f"nombre: {self.nombre}, apellido : {self.apellido}, ciudad : {self.ciudad}")

    def area(self):
        return f"El área del rectángulo es {self.largo*self.ancho}."
    
    def perimetro(self):
        return f"El perímetro del rectángulo es {2*self.largo + 2*self.ancho}."
    
    def diagonal(self):
        diagonal= (self.largo**2 + self.ancho**2)**0.5      
        return f"La diagonal de rectángulo mide {diagonal}."

# creamos objeto
rectangulin = Rectangulo(3,4)


print(rectangulin.area())
print(rectangulin.perimetro())
print(rectangulin.diagonal())
