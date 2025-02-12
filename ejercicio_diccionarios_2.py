"""
ENTRADAS DEL CINE

Vamos a crear una app para vender entradas del cine.

Hay tres precios:
- Entrada estándar: 9.00
- Mayores de 65 años (seniors) : 6.90
- Infantiles : 7.20

Se puede vender cualquier cantidad de entradas,
pero los menores siempre deber ir acompañados
de un adulto.

Al finalizar la compra mostraremos las entradas 
y el importe total. 

En cualquier momento hay que poder finalizar el proceso sin que se produzca la compra.

No se puede quitar entradas

"""

import os
os.system ("cls")

# precio entradas
general = 9
mayores = 6.9
infantil = 7.2

menu = """
1. Entrada general --> 9.00 euros 
2. Mayores de 65 años --> 6.90 euros
3. Infantiles -->7.20
4. Finalizar la compra
X. Salir
"""
print(menu)


adultos_dic={}
mayores_dic={}
niños_dic={}
precio_final=[adultos_dic,mayores_dic,niños_dic]
opcion = input("Elige tu opcion --> ").strip().lower()

while True:

    match opcion:
        case "1":

            if adultos_dic:
                cantidad_g = int(input("Cuántas entradas generales deseas? -->"))
                precio_g=cantidad_g*general
                adultos_dic["cantidad"]+=1
                adultos_dic["precio"] +=1
            else:
                cantidad_g = int(input("Cuántas entradas generales deseas? -->"))
                precio_g= cantidad_g*general
                adultos_dic.update({"cantidad":cantidad_g, "precio": precio_g })
                precio_final.append(adultos_dic)

                
            

        case "2":
            pass

        case "3":
            pass
        case "4":
            pass
        case "x":
            pass
            # print("Fin del programa")
            # break
        case _ :
            print("Opción no reconocida.\nVuélvelo a probar.")

