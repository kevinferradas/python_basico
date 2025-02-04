"""
WHILE = mientras
"""

# num = 5
# while num > 0:
#     print(num)
#     num -=1
# else:
#     print("Has entrado en el else")

# print("#"*20)
# num = 5
# while True:
#     print(num)
#     num -=1
#     if num== 0:
#         break
# else:
#     print("Has entrado en el else")

import os
os.system("cls")

monedas = 10
# if monedas==0:
#     break

while True:
    prestamo = input("¿Cuántas monedas necesitas?")

    if monedas>=int(prestamo):
        monedas -=int(prestamo)
        print(f"Quedan {monedas} monedas.")
        if monedas==0:
            print("Ya no podemos hacer más préstamos")
            break
    
    else:
        print(f"No hay suficientes monedas")
        


    


