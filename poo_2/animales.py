# Herencia
import os
os.system ("cls")

class Animal ():
    def __init__(self, especie,edad):

        # Atributos de instancia
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar (self):
        pass
    
    # Método genérico pero con implementación particular
    def moverse (self):
        pass

    # Método genérico con la misma implementación
    def describeme (self):
        print("Soy un Animal del tipo", type(self).__name__)

    # def __str__(self):
    #     return f" La especie es {self.especie}."

# CLASES HIJAS

class Perro(Animal):

    def __init__(self, especie, edad, dueño):
        # Alternativa 1
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño

        # Alternativa 2
        super().__init__(especie, edad)
        self.dueño = dueño

    def hablar (self):
        print("Guau!")
    def moverse (self):
        print ("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")



mi_perro = Perro('mamífero',10,'Luis')
mi_vaca = Vaca('mamífero', 23)
mi_abeja = Abeja('insecto', 1)

print(mi_perro.especie)
print(mi_perro.edad)
print(mi_perro.dueño)


mi_perro.hablar() # Guau!
mi_vaca.hablar() # Muuu!



mi_perro.describeme() # Soy un Animal del tipo Perro
mi_vaca.describeme() # Soy un Animal del tipo Vaca
mi_abeja.describeme() # Soy un Animal del tipo Abeja

mi_abeja.picar() # Picar!

print(Perro.__bases__)

variable = {}
print(f"{variable} es una variable de tipo '{type(variable).__name__}'")


# class Perro(Animal):
#     def sonido(self):
#         print("Guau")

# tortuga = Animal("Tortuga")

# milu = Perro ("Perro")
# milu.sonido()
# print(milu)

# class Gato(Animal):
#     def sonido(self):
#         print("Miau")

# mishi = Gato ("siamés")

# print(Perro.__bases__) # (<class '__main__.Animal'>,)
# print(Animal.__subclasses__()) # [<class '__main__.Perro'>, <class '__main__.Gato'>]

