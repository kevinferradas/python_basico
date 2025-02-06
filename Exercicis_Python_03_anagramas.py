"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 3
Un anagrama es un texto o palabra resultante de modificar el orden de otro texto o palabra.
Los textos deberán ir sin tildes (acentos o diéresis)
No se tienen en cuenta mayúsculas ni espacios.

Mostraremos el mensaje: "Anagramas"
Pediremos al usuario un texto/palabra.
Pediremos al usuario un segundo texto/palabra
Responderemos si ambos son anagramas o no.

Por ejemplo:
    "Introduzca el primer texto --> " Pedro
    "Introduzca el segundo texto --> " Poder
    "Son anagramas --> Sí"

Otro ejemplo:
    "Introduzca el primer texto --> " Ramon
    "Introduzca el segundo texto --> " Morir
    "Son anagramas --> No"
 
"""

import os
os.system ("cls")

print("Anagramas")
texto_palabra_1=input("Escribe un texto o palabra -> ")
texto_palabra_2=input("Escribe un segundo texto o palabra ->")

texto_palabra_1=texto_palabra_1.lower()
texto_palabra_1=texto_palabra_1.replace(" ","")
texto_palabra_2=texto_palabra_2.lower()
texto_palabra_2=texto_palabra_2.replace(" ","")


letras_1=[]
for letras in texto_palabra_1:
    letras_1.append(letras)
print(letras_1)
    
letras_2=[]
for letras in texto_palabra_2:
    letras_2.append(letras)
print(letras_2)

for i in range(len(letras_1)):
    if letras_1[i] not in letras_2:
        print("Son anagramas --> No")
        break
else:
    print("Son anagramas --> Sí")




