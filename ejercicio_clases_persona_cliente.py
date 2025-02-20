"""
Vamos a crear una clase llamada Persona.
Tendrá estos atributos:
-- nombre
-- apellido
-- ciudad

Crear el constructor y el método que muestra la información de la clase (print(objeto))

También habrá una clase hija llamada Cliente.

Tendrá además los atributos : 
-- dni
-- compras

Cuando se muestre el objeto, debe aparecer todos los atributos.

Hay que crear un método compras_realizadas que tenga esta salida:
El cliente Fulanito ha comprado xx.xx euros.
"""
import os
os.system ("cls")

# # Definimos la clase persona
# class Persona ():
    
#     def __init__(self, nombre: str, apellido: str, ciudad: str):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.ciudad = ciudad 


#     def __str__(self):
#         return f"nombre: {self.nombre}, apellido : {self.apellido}, ciudad : {self.ciudad}"

# persona = Persona ("Maria", "Pau", "BCN")
# # print(persona.nombre)   # Maria

# # Definimos la clase hija

# class Cliente (Persona):
#     def __init__(self, nombre: str, apellido: str, ciudad: str , dni, compras):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.ciudad = ciudad
#         self.dni = dni
#         self.compras = compras
    
#     def compras_realizadas(self):
#         return f" El cliente {self.nombre} {self.apellido} ha comprado {self.compras} euros"
        
# print(type(persona))

# cliente_1 = Cliente ("Kevin","Ferradas","Trujillo","1234",30_000)
# print("\n")
# print(cliente_1.compras_realizadas() )
# print("\n")
# print(type(cliente_1))
# print(cliente_1)
# print("\n")

##################################################################

import os
os.system ("cls")

# Definimos la clase persona
class Persona ():
    
    def __init__(self, nombre: str, apellido: str, ciudad: str):
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad = ciudad 


    def __str__(self):
        print( f"nombre: {self.nombre}, apellido : {self.apellido}, ciudad : {self.ciudad}")

persona = Persona ("Maria", "Pau", "BCN")

# Definimos la clase hija

class Cliente (Persona):
    def __init__(self, nombre: str, apellido: str, ciudad: str , dni, compras):
        super().__init__(nombre,apellido,ciudad)
        self.dni = dni
        self.compras = compras
    
    def __str__(self):
        super().__str__()
        return f"Su DNI es {self.dni}, y ha comprado {self.compras} euros."

    def compras_realizadas(self):
        return f"El cliente {self.nombre} {self.apellido} ha comprado {self.compras} euros"
        

cliente_1 = Cliente ("Kevin","Ferradas","Trujillo","1234",30_000)
print("\n")
print(cliente_1.compras_realizadas() )
print("\n")
# print(type(cliente_1)) # <class '__main__.Cliente'>
print(cliente_1)
print("\n")
