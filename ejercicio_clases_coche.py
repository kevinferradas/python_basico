"""
Crear una clase llamada Coche.

Tendrá los siguientes atributos:
-- marca
-- color
-- combustible
-- cilindrada

Crear la función __init__ con los parámetros anteriores.

Crear otra función llamada "mostrar_característica" que muestre todos los detalles anteriores en un 
único mensaje.

Crear la función __str__ que tendrá como salida la marca y el color.

Con eso crearemos un objeto Coche, con estos valores:
-- Opel
-- Rojo
-- eléctrico
-- 1.6

Ejecutar las funciones que acabas de crear.
"""
import os
os.system ("cls")

class Coche ():
    
    def __init__(self, marca, color, combustible, cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada 

    def mostrar_caracteristicas(self):
        return f"El coche es de la marca {self.marca}, es de color {self.color}, \
es tipo {self.combustible} y tiene una cilindrada de {self.cilindrada}. "

    def __str__(self):
        return f"marca: {self.marca}, color : {self.color}"
    
cochazo = Coche("Opel","rojo","eléctrico","1.6")
print("\n")
print(cochazo.mostrar_caracteristicas() )
print("\n")
print(cochazo)
print("\n")