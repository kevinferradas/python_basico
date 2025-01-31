'''
Excepciones
Son errores que se producen durante la ejecución del programa y lo interrumpen
'''
import os
os.system ("cls")

#try / except
#si hay try debe haber un except

try:
    #Intentamos ejecutar el código
    num = float(input("Escribe un número ..."))
    # print(1/0)
    # print("Después de la división por cero")
except ValueError: #Error de conversión de tipos
    print("Has de introducir un número")
except ZeroDivisionError: #Error por división por cero
    print("No se puede dividir por cero")
except: #error genérico
    print("Ha ocurrido un error")

print("El programa continúa ...")

try:
    #intenta hacer algo
    pass
except:
    #si falla ejecuta esto
    pass
else:
    #si no falla ejecuta esto
    pass
finally:
    #se ejecuta siempre
    pass
print("Aquí habrá más código")