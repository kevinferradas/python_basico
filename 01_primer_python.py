

#Esto es un comentario de una línea
numero_entero=2 # esto también funciona
numero_decimal=4.5
saludo="Buenas tardes"
despedida='Adiós'

declaration="I'm a developer"
ejemplo_comilla_triple =""" 
    estoy dentro de una 
    comilla triple 
"""

"""
Esto es un comentario

"""

verdad= True
mentira= False 
print(numero_entero)
print("numero_entero es de tipo ", type(numero_entero))
print(numero_decimal)
print(ejemplo_comilla_triple)

from datetime import datetime 
print(datetime.now())

suma = 1 + 3
reta= 1-4
multiplicacion = 4*2
division = 10/5
exponencial= 4** 0.5
division_entera= 20//6
modulo= 20%3s


print(modulo)

texto1= "buenas"
texto2= "noches"
texto_final= texto1 +" "+ texto2
print(texto_final)
texto_final=f"{texto1} {texto2}"
print(texto_final)
texto_final = "{} {}".format(texto1,texto2)
print(texto_final)