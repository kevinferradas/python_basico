'''
Crea una clase llamada Vehiculo.

En su constructor incluye marca, modelo y año de construcción.

Dos métodos también:
-- arrancar, con el mensaje "El vehículo XX modelo YY ha arrancado"
-- detener, con el mensaje "El vehículo XX modelo YY se ha detenido"

Luego, dos clases hijas: Coche y Moto

La clase Coche tiene dos atributos propio: numero de puertas y AC (verdadero o falso).
y también un método propio: abrir_maletero, que
devuelve este mensaje: "El maletero del [marca] [modelo] está abierto"

La clase Moto tiene un método propio: revisar_seguridad, devuelve este mensaje:
"Si circulas en motocicleta debes llevar casco"
'''

import os
os.system ("cls")

# Definimos la clase Vehículo
class Vehiculo ():
    
    def __init__(self, marca: str, modelo: str, any_construccion: int):
        self.marca = marca 
        self.modelo = modelo
        self.any = any_construccion 

    def arrancar(self):
        return f"El vehículo {self.marca} modelo {self.modelo} ha arrancado."
        

    def detener(self):
        return f"El vehículo {self.marca} modelo {self.modelo} se ha detenido."
     

    
# Definimos la clase hija Coche

class Coche (Vehiculo):
    def __init__(self, marca: str, modelo: str, any_construccion: int,num_puertas: int, AC:bool):        
        super().__init__(marca,modelo,any_construccion)
        self.puertas = num_puertas
        self.AC = AC
    
   

    def abrir_maletero(self):
        return f"El maletero del  {self.marca} {self.modelo} está abierto"
    
# Definimos la clase hija Moto

class Moto (Vehiculo):
    def __init__(self, marca: str, modelo: str, any_construccion: int):        
        super().__init__(marca,modelo,any_construccion)
        


    def revisar_seguridad(self):
        return f"Si circulas en motocicleta debes llevar casco"
        
cochazo = Coche("Toyota","TY2025",2025,4,True)
motazo = Moto("Mercedes","M2024",2024)
print(cochazo.arrancar())
print(cochazo.detener())
print(cochazo.abrir_maletero())
print(motazo.arrancar())
print(motazo.detener())
print(motazo.revisar_seguridad())

