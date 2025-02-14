
"""
LISTA DE MEJORAS

Limitar un máximo de partidas.
Contar cuántas veces ha ganado, perdido y empatado.
Preguntar el nombre del usuario

Guardar los resultados
"""



import os
os.system ("cls")

import random  # libreria para generar numeros aleatorios


# Lista de opciones
opciones_juego = ["Piedra", "Papel" , "Tijeras"]

opciones_juego = ['🥌', '⬜', '✂']

partidas_ganadas = 0
partidas_perdidas = 0
empates = 0

nombre_usuario = input ("Escribe tu nombre --> ")
print(f"Buena suerte {nombre_usuario} !!\n")

while True: 
    try:
        numero_partidas = int(input ("Cuántas partidas quieres jugar (entre 1 y 5, 0 para salir)? --> "))
        if numero_partidas==0:
            print (f"Hasta pronto {nombre_usuario}!")
            break
            # os.system("exit") # acaba el programa ( el break en cambio solo finalizaría el bucle)
        elif 1<= numero_partidas <=5:
            break
        else:
            print("Has de introducir un número entre 1 y 5 \n")
        

    except:
        print("Has de introducir un número entero\n.") 

contador_de_partidas = 1

# user_dic={"victorias_u":0,"derrotas_u":0,"empates_u":0}
# maquina_dic={"victorias_m":0,"derrotas_m":0,"empates_m":0}

while contador_de_partidas <= numero_partidas:
    contador_de_partidas +=1
    # print(user_dic)
    # print(maquina_dic)
# informar al usuario de las opciones del juego
    menu=f"""
    PIEDRA - PAPEL - TIJERAS
    ========================
    1. {opciones_juego[0]}
    2. {opciones_juego[1]}
    3. {opciones_juego[2]}

    Escribe cualquier otra cosa para salir.
    """
    print(menu)

    opcion_humano = input ("Elige tu opción --> ").strip()

    if opcion_humano not in ["1","2","3"]:
        print ("Juegp finalizado. Hasta pronto!")
    else:
        opcion_maquina=str(random.randint(1,3))

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
        
