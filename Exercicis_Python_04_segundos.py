"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 4
Mostraremos el mensaje: "Conversor de segundos"
A continuación pediremos al usuario una cantidad de segundos.

Le responderemos:
- Si son menos de 60 segundos, mostrará "X segundos son menos de 1 minuto"
- Si es igual o superior a 60 segundos le diremos:
    "X segundos son Y minutos y Z segundos"

Y así para las siguientes unidades de tiempo. Por tanto, si la cantidad de segundos 
supera la hora, le diremos cuantas horas, minutos y segundos son. 
Lo mismo si supera un día o una semana. 

. 
"""
import os
os.system ("cls")
print("Conversor de segundos")

try:
    segundos=int(input("Escriba una cantidad de segundos ->"))
    if segundos<60:
        print(f"{segundos} segundos son menos de 1 minuto ")
    elif 60<=segundos<3600:
        minutos_m=segundos//60
        segundos_m=segundos%60 
        print(f"{segundos} segundos son {minutos_m} minutos y {segundos_m} segundos.")
    elif  3600 <=segundos<86400:
        horas_h=segundos//3600
        minutos_h= (segundos - 3600)//60
        segundos_h=(segundos - 3600)%60
        print(f"{segundos} segundos son {horas_h} horas, {minutos_h} minutos y {segundos_h} segundos.")
    elif 86400<=segundos<604800:
        dias_d=segundos//86400
        horas_d=(segundos-86400)//3600
        minutos_d=(segundos-86400 -3600*horas_d)//60
        segundos_d=(segundos-86400- 3600*horas_d)%60
        print(f"{segundos} segundos son {dias_d} días, {horas_d} horas, {minutos_d} minutos y {segundos_d} segundos.")
    elif 604800<=segundos<2419200:
        semanas_s=segundos//604800
        dias_s=(segundos-604800)//86400
        horas_s=(segundos-604800-86400*dias_s)//3600
        minutos_s=(segundos-604800-86400*dias_s-3600*horas_s)//60
        segundos_s=(segundos-604800-86400*dias_s-3600*horas_s)%60
        print(f"{segundos} segundos son {semanas_s} semanas, {dias_s} días, {horas_s} horas, {minutos_s} minutos y {segundos_s} segundos.")

except:
    print("Debe introducir los segundos de manera numérica")

