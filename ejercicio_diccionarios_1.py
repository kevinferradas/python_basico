"""
EJERCICIO DICCIONARIOS
"""
"""
Tenemos un sitio que registra los accesos de los usuarios.
Necesitamos un menú con estas opciones
1. Añadiremos un usuario (si no existe)
2. Añadiremos una visita al usuario indicado. ( si el usuario no existe mostrar el error)
3. Mostraremos las visitas del usuario que se decida ( si el usuario no existe mostrar el error)
4. Mostraremos las visitas de todos los usuarios (si no hay usuarios todavía indicarlo)
X. Salir

Asumimos que los nombres de los usuarios no se repiten.
Hazlo como quieras.
"""




# lista_acciones=["Añadir usuario","Añadir visita","Mostrar visitas","Mostrar visitas de todos los usuarios","Salir"]
# # menu=[1,2,3,4,"X"]


# for item in lista_acciones:
#     indice= lista_acciones.index(item)
#     if item == lista_acciones[-1]:
#         print(f"X. {item}")
#     else:
#         print(f"{indice +1 }. {item}")


# accion=input("Escoja la acción que desea realizar -> ")

# while accion != "X":

#     # si escoge 1
#     lista_usuarios=[] #usuarios={dic_user1,dic_user2,...}
#     if int(accion) == 1:

#         nombre_usuario=input("Introduzca el nombre del usuario -> ")
#         dic_usuario = {"Nombre" : nombre_usuario, "Visitas": 0}
#         lista_usuarios.append(dic_usuario)
#         print(lista_usuarios)

#     elif int(accion) == 2:

#         nombre_usuario=input("Introduzca el nombre del usuario -> ")
#         dic_usuario["Visitas"] += 1

#     elif int(accion) == 3:
#         nombre_usuario=input("Introduzca el nombre del usuario -> ")
#         print(dic_usuario.get("Visitas",f"El usuario insertado no existe"))

#     elif int(accion) == 4:
#         nombre_usuario=input("Introduzca el nombre del usuario -> ")



#SOLUCION 

import os
os.system ("cls")

lista_usuarios=[]
while True:
    menu = """
1. Añadiremos un usuario (si no existe)
2. Añadiremos una visita al usuario indicado. ( si el usuario no existe mostrar el error)
3. Mostraremos las visitas del usuario que se decida ( si el usuario no existe mostrar el error)
4. Mostraremos las visitas de todos los usuarios (si no hay usuarios todavía indicarlo)
X. Salir
"""
    print(menu)
    opcion = input("Elige tu opcion --> ").strip().lower()

    
    match opcion:
        case "1":
            nombre_usuario=input("Introduzca el nombre del usuario -> ").strip().title()
            
            if lista_usuarios:
                for usuario in lista_usuarios:
                    if usuario["Nombre"] == nombre_usuario:
                        print("El usuario introducido ya existe.")
                        print(85,lista_usuarios)
                        # break
                    else:
                        dic_usuario = {"Nombre" : nombre_usuario, "Visitas": 0}
                        lista_usuarios.append(dic_usuario)
                        print(90,lista_usuarios) 
                        # break
            else:
                dic_usuario = {"Nombre" : nombre_usuario, "Visitas": 0}
                lista_usuarios.append(dic_usuario)
                print(95, lista_usuarios)

    
        case "2":
            nombre_usuario=input("Introduzca el nombre del usuario -> ")

            if lista_usuarios:
                for usuario in lista_usuarios:
                    if usuario["Nombre"] == nombre_usuario:
                        usuario["Visitas"] += 1
                    else:
                        print("El usuario indicado no existe")
                        print(lista_usuarios)
            else:
                print("Debe crear primero un usuario, marcando la opción 1.")


        case "3":
            nombre_usuario=input("Introduzca el nombre del usuario -> ")
            print(dic_usuario.get("Visitas",f"El usuario insertado no existe"))
        case "4":
            nombre_usuario=input("Introduzca el nombre del usuario -> ")
        case "x":
            print("Fin del programa")
            break
        case _ :
            print("opción no reconocida. \nVuélvelo a probar.")