
"""
LISTA DE MEJORAS

Limitar un máximo de partidas.
Contar cuántas veces ha ganado, perdido y empatado.
Preguntar el nombre del usuario

Guardar los resultados
"""




import random  # libreria para generar numeros aleatorios
import os
os.system ("cls")

# Lista de opciones
opciones_juego = ["Piedra", "Papel" , "Tijeras"]

opciones_juego = ['🥌', '⬜', '✂']

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
        print("Empate")
    elif (opcion_humano =="1" and opcion_maquina=="3")  or \
        (opcion_humano =="2" and opcion_maquina=="1")  or \
         (opcion_humano =="3" and opcion_maquina=="2"):
        print("Has ganado!!")
    else:
        print("Has perdido!!")

        
