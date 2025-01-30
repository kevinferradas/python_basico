"""
IF/ELIF/ELSE
Control de condiciones
"""

# # Condición binaria
# llueve = False

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

# Preguntar al usuario la edad
# si tiene menos de 0 o más de 120 diremos: no me lo creo
# si tiene menos de 18 años diremos : aún no puedes votar, te faltan x años
# si tiene 18 o más, diremos : puedes votar desde hace x años

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


# Ejercicio
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
numero_1= input("Escribe el primer número -> ")
# numero_1=int(numero_1)
numero_2= input("Escribe el segundo número -> ")
# numero_2=int(numero_2)
operacion= input("Escribe la operación matemática que deseas hacer -> ")

if numero_1.isalpha()==True:
    print("Debe introducir un número")
elif numero_2.isalpha()==True:
    print("Debe introducir un número")
elif operacion == "suma":
    print(float(numero_1)+float(numero_2))
elif operacion== "resta":
    print(float(numero_1)-float(numero_2))
elif operacion== "multi":
    print(float(numero_1)*float(numero_2))
elif operacion == "exp":
    print(float(numero_1)**float(numero_2))
elif operacion == "division":
    if float(numero_2)==0:
        print("No es posible dividir por cero")
    else:
        print(float(numero_1)/float(numero_2))
elif operacion == "div_ent":
    if float(numero_2)==0:
        print("No es posible dividir por cero")
    else:
        print(float(numero_1)//float(numero_2))        
elif operacion == "modulo":
    if float(numero_2)==0:
        print("No es posible dividir por cero")
    else:
        print(float(numero_1)%float(numero_2))
else:
    print("Debe elegir una operación matemática ")



