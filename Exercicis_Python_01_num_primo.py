"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 1

Un número primo es aquel que sólo es divisible por sí mismo o uno.

Pediremos al usuario un número entero.
Si escribe algo que no sea un número entero la aplicación debe responder: 
    "Has de introducir un número entero".
Daremos hasta tres oportunidades para que nos facilite un dato correcto.
Pero si pasadas esas tres oportunidades sigue sin escribir un entero 
la aplicación finalizará mostrando este mensaje:
    "No has podido introducir un número entero en tres oportunidades
    Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.
    ".
Si escribe un número entero puede pasar que
-- sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X es primo".
-- no sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X no es primo".

. 
"""
import os
os.system ("cls")



# Todos los números son divisibles por 1 y por ellos mismos
# Para comprobar que el número es primo, intentaremos descubrir si es divisible por algún número en el intervalo [2,numero].
#Por otro lado, el máximo divisor posible de un número,dejando de lado el mismo número es su mitad. Ej: 20: 1,2,4,5,10,20. 
#Luego, solo hará falta descubrir si es divisible por algún número en el intervalo [2,numero/2]

intentos=1 
# El usuario tiene máximo 3 intentos.
while intentos <= 3: #Para ejecutar el código mientras los intentos 
    try:
        print(f"Intento número {intentos }")
        numero= int(input("Escribe un número entero -> ")) 
        # print(numero)
        for x in range(2,(numero//2) +1): 
            if numero % x ==0: 
                print(f"El número {numero} no es primo.") 
                break
        else: #si el número no es divisble por ningún número en el rango indicado, la única opción es que se trate de un número primo
            print(f"El número {numero} es primo") 
        break
    except ValueError:
        intentos +=1
        if intentos <=3:
            print("Has de introducir un númnero entero")
            
            # print(intentos)
        
else:
    print("No has podido introducir un número entero en tres oportunidades \nPuedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.")




    
    

        



        


    