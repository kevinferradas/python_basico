"""
BOOLEANS
"""

verdadero= True
falso= False 
Verdadero= True

print(id(verdadero))
print(id(Verdadero))
print(id(falso))

print(verdadero is Verdadero) 
#Algunos valores tienen asignado False
#0 -> el número 0
# "" -> string vacío
# [] -> lista vacía

print(bool(0))

if 0:
    print("El 0 es verdadero")
else:
    print("El 0 es falso")

if []:
    print("")

