
"""
LISTA DE MEJORAS

Limitar un máximo de partidas.
Contar cuántas veces ha ganado, perdido y empatado.
Preguntar el nombre del usuario

Guardar los resultados
"""



import os
os.system ("cls")

import random  # importamos el módulo random


# Lista de opciones
# opciones_juego = ["Piedra", "Papel" , "Tijeras"]

# Lista de opciones
opciones_juego = ['🥌', '⬜', '✂']

# Declaramos las variables que contarán las victorias, derrotas, y empates, respectivamente.
# Le asignamos el valor inicial de cero.
partidas_ganadas = 0
partidas_perdidas = 0
empates = 0

# Le pedimos al usuario que ingrese su nombre.
nombre_usuario = input ("Escribe tu nombre --> ")
print(f"Buena suerte {nombre_usuario} !!\n")


# Definimos la acción a realizar por el usuario ( jugar o salir de la aplicación ).
while True: 
    try:

        # Preguntamos al usuario la cantidad de partidas que desea jugar (entre 1 y 5).
        # Si desea salir, le indicamos que escriba el número "0".
        numero_partidas = int(input ("Cuántas partidas quieres jugar (entre 1 y 5, 0 para salir)? --> "))

        # Si el usuario escribe "0", mostramos mensaje de despedida y salimos de la aplicación.
        if numero_partidas==0:
            print (f"Hasta pronto {nombre_usuario}!")
            break
            # os.system("exit") # acaba el programa ( el break en cambio solo finalizaría el bucle)

        # Si el usuario escribe un número entero del 1 al 5,
        elif 1<= numero_partidas <=5:
            break

        
        else:
            # Si el usuario escribe un número menor a 1 o mayor a 5, se mostrará el siguiente mensaje
            print("Has de introducir un número entre 1 y 5 \n")
        
    
    except:
        # Si el usuario introduce un carácter no numérico, o un decimal, se mostrará el siguiente mensaje
        print("Has de introducir un número entero\n.") 

# Declaramos una variable que contará la cantidad de partidas que el usuario vaya jugando.
# Tendrá el valor inicial de 1
contador_de_partidas = 1

# user_dic={"victorias_u":0,"derrotas_u":0,"empates_u":0}
# maquina_dic={"victorias_m":0,"derrotas_m":0,"empates_m":0}

# El siguiente código se ejecuta mientras no se supere la cantidad de partidas establecida por el usuario.
while contador_de_partidas <= numero_partidas:

    contador_de_partidas +=1

    # print(user_dic)
    # print(maquina_dic)

    # Informar al usuario de las opciones del juego: 1.Piedra , 2. Papel, 3. Tijera
    menu=f"""
    PIEDRA - PAPEL - TIJERAS
    ========================
    1. {opciones_juego[0]} 
    2. {opciones_juego[1]} 
    3. {opciones_juego[2]}

    Escribe cualquier otra cosa para salir.
    """

    # Mostramos el menú al usuario.
    print(menu)

    # Pedimos al usuario que elija su opción (1,2 o 3).
    # El .strip() es en caso el usuario inserte , además del número, uno o más espacios. 
    opcion_humano = input ("Elige tu opción --> ").strip()

    # Si el usuario inserta algo distinto a 1,2 o 3, mostramos mensaje de despedida al usuario.
    if opcion_humano not in ["1","2","3"]:
        print ("Juego finalizado. Hasta pronto!")

    # Si el usuario inserta 1,2 o 3, se ejecuta el siguiente código.
    else:
        
        # La opción de la máquina será generada de manera aleatoria con la función
        opcion_maquina=str(random.randint(1,3)) # Llama a la función randint del módulo random.


        resultado_partida = f"""
        Has elegido {opciones_juego[int(opcion_humano)-1]}
        La máquina ha elegido {opciones_juego[int(opcion_maquina)-1]}
    """ 
        print(resultado_partida)
        
        if opcion_humano == opcion_maquina:
            empates += 1
            print(f"{nombre_usuario}, habéis empatado.")
            # user_dic["empates_u"] +=1
            # maquina_dic["empates_m"] +=1

        elif (opcion_humano =="1" and opcion_maquina=="3")  or \
            (opcion_humano =="2" and opcion_maquina=="1")  or \
            (opcion_humano =="3" and opcion_maquina=="2"):
            partidas_ganadas +=1
            print(f"{nombre_usuario}, Has ganado!!")
            # user_dic["victorias_u"] +=1
            # maquina_dic["derrotas_m"] +=1

        else:
            print(f"{nombre_usuario} Has perdido!!")
            partidas_perdidas +=1
            # user_dic["derrotas_u"] +=1
            # maquina_dic["victorias_m"] +=1
        
        resultado_actual = f"""
    Ganadas: {partidas_ganadas} | Empates : {empates} | Perdidas : {partidas_perdidas}
        \n\n    
"""     
        print(resultado_actual)

print("Aplicación finalizada.")
        
