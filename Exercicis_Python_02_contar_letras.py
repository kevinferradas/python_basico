"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 2a

Mostraremos el texto: "Contar letras en un texto"

Pediremos al usuario un texto, así:
"Por favor, introduzca un texto "
Puede contener números y caracteres con tilde.

A continuación mostraremos las letras que contiene y cuantas son,
ordenadas por número de apariciones. En caso de empate, en orden alfabético. 
Ignoraremos los números, los espacios y los signos de puntuación 
(punto, coma, punto y coma, exclamación, etc.)
Consideremos mayúsculas y minúsculas como la misma letra.

Por ejemplo:
"Por favor, introduzca un texto " ¿Amar?
La respuesta sería: 
"El texto contiene las letras:
a, 2 veces
m, 1 vez
r, 1 vez
"

Por ejemplo:
"Por favor, introduzca un texto " Python forever and ever
La respuesta sería: 
"El texto contiene las letras:
e, 4 veces
r, 3 veces
o, 2 veces
n, 2 veces
a, 1 vez
f, 1 vez
h, 1 vez
p, 1 vez
v, 1 vez
y, 1 vez
"
"""

import os
os.system ("cls")
# signos=["¡","!","¿","?",",",";",":"," "]
# texto=input("Por favor, introduzca un texto -> ")

# for signo in signos:
#     texto=texto.replace(signo,"")

# texto=texto.lower()
# texto=texto.replace("á","a")
# texto=texto.replace("é","e")
# texto=texto.replace("í","i")
# texto=texto.replace("ó","o")
# texto=texto.replace("ú","u")
# # texto=texto.replace(" ","")

# print(texto)
# for letra in texto:
#     contador=texto.count(letra)
#     if contador>1:
#         print(f"{letra}, {contador} veces ")
#     if contador==1:
#         print(f"{letra}, {contador} vez ")
    






"""  
Ejercicio 2b

Mostraremos el texto: "Contar palabras en un texto"
Lo mismo que el ejercicio anterior, pero con palabras en lugar de letras.
"""
print("Contar las palabras en un texto")
signos=["¡","!","¿","?",",",";",":"]
texto=input("Por favor, introduzca un texto -> ")

for signo in signos:
    texto=texto.replace(signo,"")

texto=texto.lower()
lista_palabras=texto.split(" ")

print(texto)

for palabra in lista_palabras :
    contador=lista_palabras.count(palabra)
    print(f"{palabra}->{contador}")



