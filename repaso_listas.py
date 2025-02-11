"""
REPASO LISTAS
Es una colección MUTABLE de datos.
"""

import os
os.system ("cls")

# lista vacía
lista = []

lista.append("Anna")
print(lista) #["Anna"]
lista[0] = "Marta"
print(lista) #["Marta"]

# Las listas son colecciones de datos indexados
# el índice empieza en 0
lista[0]

lista_enteros = list(range(1,21,2)) #casting
print(lista_enteros)

lista_nombres = ["Pol", "Noa", "Sara", "Pepe"]
# indices -->      0      1       2       3


for nombre in lista_nombres:
    indice=lista_nombres.index(nombre) # devuelve el índice que se corresponde con el valor
    print(f"{indice}. {nombre}")

for indice, valor in enumerate(lista_nombres):
    print(f"{indice}.{valor}")

# Copia de una lista

nueva_lista_1 = lista_nombres.copy()
nueva_lista_2 = lista_nombres[:] # solo en python

# Mini ejercicio: obtener los números elevados al cuadrado de la serie.
lista_numeros= list(range(0,11))

for numeros in lista_numeros:
    print(f"{numeros**2}")

# Necesitamos otra lista sólo con los números elevados al cuadrado de lista_números:

lista_cuadrados=[]
for numeros in lista_numeros:
    cuadrado=numeros**2
    lista_cuadrados.append(cuadrado)
    
print(lista_cuadrados)

#SOLUCION FERRAN 

# Forma 1

lista_cuadrados=[]
for numero in lista_numeros:
    lista_cuadrados.append(numeros**2)   
print(lista_cuadrados)


# Forma 2 --> List comprehensions
lista_cuadrados = print([numero**2 for numero in lista_numeros])


for index, valor in enumerate(lista_numeros):
    lista_numeros[index]=valor**2

print(lista_numeros)

lista_ciudades = ["NY", "LA", "BCN"]
ny, la, bcn = lista_ciudades
print(bcn)