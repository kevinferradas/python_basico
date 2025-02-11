"""
TUPLAS
Es una colección INMUTABLE de datos
"""
mi_tupla= (3,)# tambien 3,  #tambien 3,4,5
print(type(mi_tupla))

tupla =("Anna","Pou", 20 , "anna@email.com")
print(tupla)
# tupla[0] = "Marta" --> no  funciona, las tuplas son inmutables
lista_temporal=list(tupla)
print(lista_temporal)
lista_temporal[0]= "Marta"
print(lista_temporal)
tupla=tuple(lista_temporal)
print(tupla)
print(tupla[1:3]) # slicing

for item in tupla:
    print(item)