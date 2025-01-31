"""
PROPIEDADES DE LOS NÚMEROS 

"""

# OPERACIONES MATEMÁTICAS

suma = 1 + 3
resta= 1-4
multiplicacion = 4*2
division = 10/5
exponencial= 4** 0.5
division_entera= 20//6
modulo= 20%3

# Precedencia de las operaciones -> pon paréntesis
operacion= (1 + 2) - (3*(4/5)) 

print(type(operacion)) 

# OPERACIONES DE COMPARACIÓN
# El resultado de una comparación SIEMPRE es un booleano.
#comparar si dos números son iguales
comparacion_1 = 1 == 2 
print(comparacion_1)

# comparar si dos números son diferentes
comparacion_2= 1 !=2
print(comparacion_2)

#comparar si un número es mayor que otro
print (1>2) #False
print (1>1) #False
print(1>=1) # True

#comparar si un número es menor que otro
print (1<2) #True
print (1<1) #False
print(1<=1) # True

# True = False # Error crítico de sintáxis

"""
MÉTODOS PARA NÚMEROS
"""
#redondear un número a la izquierda o derecha
redondear_izquierda= round(3.14159265359, 2) 