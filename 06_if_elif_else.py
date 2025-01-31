"""
IF/ELIF/ELSE
Control de condiciones
"""

# # Condición binaria
#  llueve = False

# if llueve:
#     print("Cogeré el paraguas")
# else:
#     print("iré a pasear")

# print("Resto del código")

lunes = False # los lunes como pizza
jueves= True  # los jueves como paella 
#el resto de días un bocadillo

# if lunes:
#     print("toca pizza") 
# elif jueves:
#     print("toca paella")
# else:
#     print("toca bocadillo") 

#Ejercicio:
# preguntar la edad al usuario
#si tiene menos de 12 años -> eres un niño/a
#si tiene menos de 18 años -> eres un/a adolescente
#si tiene menos de 30 años -> eres muy joven
#si tiene menos de 40 años -> eres joven, pero menos
#si tiene más de 40 años -> tú puedes con todo

# edad=input("Escribe tu edad -> ")
# edad=int(edad)
# if edad<0:
#     print('No es posible una edad negativa')
# elif edad < 12:
#     print("eres un niño/a")
# elif edad<18: 
#     print(" eres un/a adolescente")
# elif edad<30:
#     print("eres muy joven")
# elif edad<40:
#     print("eres joven, pero menos")
# else:
#     print("tú puedes con todo")

"""  
EJERCICIO EDAD
"""

# Preguntar al usuario la edad
# si tiene menos de 0 o más de 120 diremos: no me lo creo
# si tiene menos de 18 años diremos : aún no puedes votar, te faltan x años
# si tiene 18 o más, diremos : puedes votar desde hace x años

#SOLUCION KEVIN 1
# edad=input("Escribe tu edad -> ")
# edad=int(edad)
# diferencia_edad= 18- edad
# if edad<0  :
#     print('No me lo creo')
# elif edad>120:
#     print('No me lo creo')
# elif edad < 18:
#     print(f" Aún no puedes votar, te faltan {diferencia_edad} años")
# else: 
#     print(f" Puedes votar desde hace {-diferencia_edad} años")

#SOLUCION KEVIN 2
# edad=input("Escribe tu edad -> ")
# edad=int(edad)
# if edad<0  :
#     print('No me lo creo')
# elif edad>120:
#     print('No me lo creo')
# elif edad < 18:
#     print(f" Aún no puedes votar, te faltan {18- edad} años")
# else: 
#     print(f" Puedes votar desde hace {edad-18} años")

#SOLUCION FERRÁN

# Variable para determinar la mayoría de edad
# mayoria_edad=18
# # Obtenemos la edad del usuario
# edad = input("Por favor indica tu edad -> ")


#Ninguno de estos métodos sirven para decimales
# print(edad.isdigit())
# print(edad.isdecimal())
# print(edad.isnumeric())
# print(edad.isalpha()) 

# if not edad.isdigit(): # Comprobando que no se ha introducido un número entero
#     print("Debes introducir un número entero")
# elif 0>int(edad) > 120: # Comprobación del rango de edad válida
#     print("No me lo creo")
# else:
#     edad= int(edad) # Convertimos la edad a un número
#     diferencia=abs(mayoria_edad - edad)
#     if edad < mayoria_edad:
#         print(f"Aún no puedes votar, te faltan {diferencia} años.")
#     else:
#         print(f"Puedes votar desde hace {diferencia} años")



"""  
EJERCICIO CALCULADORA
"""
#Pedir al usuario un número
#Pedir otro número
#si no son números cada uno, le diremos que no se puede hacer
#Pedir qué operación matemática quiere hacer (7 posibilidades)
#suma
#resta
#multi
#division
#exp
#div_ent
#modulo
#pero si no es ninguna de estas, mostraremos un mensaje de error
#si divide por cero, tambien
#al dinal debe aparecer algo así :

# #SOLUCIÓN KEVIN  
# numero_1= input("Escribe el primer número -> ")
# # numero_1=int(numero_1)
# numero_2= input("Escribe el segundo número -> ")
# # numero_2=int(numero_2)
# operacion= input("Escribe la operación matemática que deseas hacer -> ")

# if numero_1.isalpha()==True:
#     print("Debe introducir un número")
# elif numero_2.isalpha()==True:
#     print("Debe introducir un número")
# elif operacion == "suma":
#     print(float(numero_1)+float(numero_2))
# elif operacion== "resta":
#     print(float(numero_1)-float(numero_2))
# elif operacion== "multi":
#     print(float(numero_1)*float(numero_2))
# elif operacion == "exp":
#     print(float(numero_1)**float(numero_2))
# elif operacion == "division":
#     if float(numero_2)==0:
#         print("No es posible dividir por cero")
#     else:
#         print(float(numero_1)/float(numero_2))
# elif operacion == "div_ent":
#     if float(numero_2)==0:
#         print("No es posible dividir por cero")
#     else:
#         print(float(numero_1)//float(numero_2))        
# elif operacion == "modulo":
#     if float(numero_2)==0:
#         print("No es posible dividir por cero")
#     else:
#         print(float(numero_1)%float(numero_2))
# else:
#     print("Debe elegir una operación matemática ")

#SOLUCIÓN CON EXPECIONES:

import os
os.system ("cls")

# # Se puede producir una excepción a causa de lo que introduzca el usuario
# try:
#     #Pedimos los números 
#     num_1 = float(input("Escribe el primer número ..."))
#     num_2 = float(input("Escribe el segundo número ..."))
#     print('''

# Opciones:
#           suma
#           resta
#           multiplicacion
#           division
#           division_entera
#           exponente
#           modulo

# ''')
#     operacion= input("Escribe la operación matemática que deseas hacer -> ")

#     if operacion == "suma":
#         print(num_1+num_2)
#     elif operacion== "resta":
#         print(num_1-num_2)
#     elif operacion== "multi":
#         print(num_1*num_2)
#     elif operacion == "exp":
#         print(num_1**num_2)
#     elif operacion == "division":
#         print(num_1/num_2)
#     elif operacion == "div_ent":
#         print(num_1//num_2)        
#     elif operacion == "modulo":
#         print(num_1%num_2)
#     else:
#         print("Debe elegir una operación matemática ")

# except ValueError:
#     print("Debes introducir un número válido en cifras")
# except ZeroDivisionError:
#     print ("No se puede dividir por cero")

#SOLUCION CON MATCH

import os
os.system ("cls")

# try:
#     #Pedimos los números 
#     num_1 = float(input("Escribe el primer número ..."))
#     num_2 = float(input("Escribe el segundo número ..."))
#     print('''

# Opciones:
#           suma
#           resta
#           multiplicacion
#           division
#           division_entera
#           exponente
#           modulo

# ''')
#     operacion= input("Escribe la operación matemática que deseas hacer -> ")

#     match operacion:
#         case "suma":
#             print(num_1+num_2)
#         case "resta":
#             print(num_1-num_2)
#         case "multiplicacion":
#             print(num_1*num_2)
#         case "division":
#             print(num_1/num_2)
#         case "division_entera":
#             print(num_1//num_2)
#         case "exponente":
#             print(num_1**num_2)
#         case "modulo":
#             print(num_1%num_2)
#         case _ : 
#             print("Debe elegir una operación matemática ")

# except ValueError:
#     print("Debes introducir un número válido en cifras")
# except ZeroDivisionError:
#     print ("No se puede dividir por cero")


#SOLUCION 3

# import os
# os.system ("cls")

# try:
#     respuesta = input ("indique los números y la operación a realizar. \n Ejemplo: 10, 5, +\n").split(", ")
#     num_1=float(respuesta[0])
#     num_2=float(respuesta[1])
#     operacion=respuesta[2]

    

#     match operacion:
#         case "+":
#             print(num_1+num_2)
#         case "-":
#             print(num_1-num_2)
#         case "x":
#             print(num_1*num_2)
#         case "/":
#             print(num_1/num_2)
#         case "//":
#             print(num_1//num_2)
#         case "^":
#             print(num_1**num_2)
#         case "%":
#             print(num_1%num_2)
#         case _ : 
#             print("Debe elegir una operación matemática ")

# except ValueError:
#     print("Debes introducir un número válido en cifras")
# except ZeroDivisionError:
#     print ("No se puede dividir por cero")



#SOLUCION 4

# import os
# os.system ("cls")

# try:
#     respuesta = input ("indique los números y la operación a realizar. \n Ejemplo: 10, 5, +\n").split(", ")
#     num_1=float(respuesta[0])
#     num_2=float(respuesta[1])
#     operacion=respuesta[2]

#     match operacion:
#         case "+"|"-"|"*"|"/"|"**"|"//"|"%":
#             resultado= eval(f"{num_1} {operacion} {num_2}")
#             print(f"{num_1} {operacion} {num_2} = {resultado}")
#         case _ :
#             print("Debe elegir una operación matemática ")


# except ValueError:
#     print("Debes introducir un número válido en cifras")
# except ZeroDivisionError:
#     print ("No se puede dividir por cero")


#EJERCICIO PALÍNDROMO

# import os
# # os.system ("cls")

# texto=input("Escriba la frase que desee : \n")
# texto=texto.strip()
# #print(texto)
# texto=texto.split()
# #print(texto)
# texto="".join(texto)
# #print(texto)
# texto=texto.lower()
# print(texto)
# texto_inv=texto[::-1]
# if texto==texto_inv:
#     print("El texto es palíndormo")
# else:
#     print("El texto no es palíndromo")


#EJERICICO PAR O IMPAR

numero=input("Escriba un número : \n")
paridad=int(numero)%2
if paridad==0:
    print("El número es par")
else:
    print("El número es impar")
    











