"""
for
"""

# nombres = ["Pol", "Pau", "Luis" , "Juan", "Pablo", "paco"]


#para cada nombre em nombres.... 
# for nombre in nombres: 
#     print(nombre)

"""
Ejercicio 1
"""
# EJERCICIO:imprimir nombres que empiecen por p

#SOLUCION KEVIN
# lista=[]
# for nombre in nombres :
#     # nombre=nombre.lower()
#     if nombre.startswith("P"):
#         lista.append(nombre)
#     print(lista)

# for x in lista:
#     print (x)
    

#SOLUCION FERRAN

# import os
# os.system("cls")

# check="P"
# #Crear el bucle para acceder a cada elemento de la lista
# for nombre in nombres:
#     # if nombre[0].lower()==check.lower():
#     #     print(nombre.capitalize())
#     if nombre.lower().startswith(check.lower()):
#         print(nombre.capitalize())


"""
Ejercicio 2
"""
#Mostrar los nombres que empiezan por 2
        
import os
os.system("cls")

edades= [25,30,35,40,45, 28, 24, 76, 89, 234]

#SOLUCION KEVIN
# check="2"

# #Crear el bucle para acceder a cada elemento de la lista
# for edad in edades:
#     if str(edad)[0]==check:
#         num_2 = edad
#         print(num_2)

#Suma total de los numeros que empiecen por 2 
# check="2"
# suma=0

# for edad in edades:
#     if str(edad)[0]==check:
#         suma += edad        
# print(suma)
   
#SOLUCION FERRAN

# check= 2
# suma = 0
# for edad in edades:
#     if str(edad).startswith(str(check)):
#         print(edad, end=" ")
#         suma +=edad
# print(end= "\n")
# print(suma)

"""
Ejercicio 3
"""

# Mostrar el resultado así:
"""
la suma de los elementos es x
Hay x elementos
el promedio de la lista es x
"""
# len_edades=len(edades)
# suma=0
# for edad in edades:
#     suma +=edad
# promedio=suma/len_edades
# print(f"La suma de los elementos es {suma}")
# print(f"Hay {len_edades} elementos")
# print(f"El promedio de la lista es {promedio}")

"""
Ejercicio 4
"""
#Mostrar si un nombre está en lista
import os
os.system("cls")

nombres = ["Pol", "Pau", "Luis" , "Juan", "Pablo", "paco"]

nombre_a_buscar= "Paco" # "Alba"
# "Luis está en la lista"
#"Alba no está en la lista"

# for nombre in nombres:
#     print(nombre)
#     if nombre.lower()== nombre_a_buscar.lower():
#         print(f"{nombre_a_buscar} está en la lista.")
#         break
# else:
#     print(f"{nombre_a_buscar} no está en la lista")

# Quiero saber qué nombres de la lista contienen con la letra "o"

# nombres_con_o=[]
# for nombre in nombres:
#     indice = nombres.index(nombre) 
#     if "o" in nombre.lower():
#         print(f"{indice + 1}. {nombre}")
#         nombres_con_o.append(nombre)
# print(nombres_con_o)

# print(list(range(10)))

# for num in range(10):
#     print(num)


for index in range(len(nombres)):
    print(f"{index}. {nombres[index]}")



