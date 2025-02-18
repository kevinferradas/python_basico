# Herencia

class Animal ():
    def __init__(self, especie):
        self.especie = especie

    def __str__(self):
        return f" La especie es {self.especie}."

class Perro(Animal):
    def sonido(self):
        print("Guau")

tortuga = Animal("Tortuga")

milu = Perro ("Perro")
milu.sonido()
print(milu)

class Gato(Animal):
    def sonido(self):
        print("Miau")

mishi = Gato ("siamés")

print(Perro.__bases__)
print(Animal.__subclasses__())