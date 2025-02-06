
"""

El usuario introduce un número entero, como máximo 100.
ese número es el límite
Desde 0 hasta el número introducido (los dos incluidos), vamos a listar todos los números:
Pero:
 -- Si el número es múltiplo de 3, escribiremos 3 - FIZZ
 -- Si el número es múltiplo de 5, escribiremos 3 - BUZZ
 -- Si el número es múltiplo de 3 y 5, escribiremos 3 - FIZZ - BUZZ
 -- En los demása casos solo el número.
 -- Si el usuario escribe más de 100 o menos de 0, diremos "El número es incorrecto"
"""
import os
os.system ("cls")

#SOLUCION KEVIN
# try: 
#     numero=int(input("Escribe un número -> "))
#     if numero<0 or numero>100:
#         print("El número es incorrecto")
        
#     else:
#         for i in range(numero + 1):
#             if i % 3 ==0 and i % 5 == 0:
#                 print(f"{i} - FIZZ - BUZZ")
#             elif i % 3 == 0:
#                 print(f"{i} - FIZZ")
#             elif i % 5 ==0:
#                 print(f"{i} - BUZZ")
#             else:
#                 print(f"{i}")
# except ValueError:
#     print("Has de escribir un número entero")

#SOLUCION FERRAN

# try:
#     referencia = int(input("Indica el número de referencia -> "))
#     # if referencia <0 or referencia > 100:
#     #      print("El número es incorrecto")
#      #     exit() 
#     if 0<= referencia <= 100:
#         for num in range(0,referencia + 1,1):
#             if num == 0:
#                 print(0)
#             elif num % 3 == 0 and num % 5 == 0:
#                 print(f"{num} - FIZZBUZZ")
#             elif num % 3 == 0:
#                 print(f"{num} - FIZZ")
#             elif num % 5 == 0:
#                 print(f"{num} - BUZZ")
#             else:
#                 print(f"{num}")    
#     else:
#         print("El número es incorrecto")
# except:
#     print("Ha de ser un número entero")



"""
Vamos a recibir un texto por parte del usuario
Con ese texto vamos a generar otro sin las vocales ni los espacios

"""
#SOLUCION KEVIN
# texto=input("Escriba un texto ->")

# vocales_espacio=["a","e","i","o","u", " "]

# for vocal in vocales:
#     texto=texto.replace(vocal,"")

# # texto=texto.replace(" ","")
# print(texto)

# #SOLUCION FERRAN
# texto=input("escribe un texto -> ").lower
# exclusiones="aeiou"
# exclusiones=["a","e","i","o","u", " ", "á"]

# for caracter in exclusiones:
#     texto = texto.replace(caracter,"")

# print(texto)

"""
Pedimos al usuario un número
Con él imprimiremos la tabla de multiplicar del 1 al 10.
"""
# try:
#     numero= int(input("Escribe un número -> "))
#     #tabla de multiplicar
#     for i in range(1,11,1):
#         print(f"{numero}x{i}={numero*i}")


# except:
#     print("Debes escribir un número")


"""
Tenemos esta lista de animales:
["gato", "perro","caballo", "paloma", "murcielago", "leon", "mono"]

Vamos a pedir una letra al usuario y mostraremos los animales que contienen esa letra.
Si no hay ninguno diremos "ningún animal contiene esa letra"
"""
animales= ["gato", "perro","caballo", "paloma", "murcielago", "leon", "mono"]
letra=input("Escribe una letra -> ")

for animal in animales:
    if letra in animal:
        print(animal)
else:
    print("Ningún animal contiene esa letra")



