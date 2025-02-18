"""
Devolver la edad a partir de dos fechas

Params
fecha_nacimiento: str -> "dd/mm/aaaa"
fecha_actual: str -> "dd/mm/aaaa"

Return
edad: int

Códigos de error: 
-1 : día o mes incorrecto
-2 : la fecha de nacimiento debe ser igual o menor que la actual
"""
import os
os.system ("cls")

def calcula_edad( fecha_nacimiento : str , fecha_actual : str) -> int :

    """
Devolver la edad a partir de dos fechas

Params
fecha_nacimiento: str -> "dd/mm/aaaa"
fecha_actual: str -> "dd/mm/aaaa"

Return
edad: int

Códigos de error: 
-1 : día o mes incorrecto
-2 : la fecha de nacimiento debe ser igual o menor que la actual
"""

    nacimiento_lista = fecha_nacimiento.split("/")
    actual_lista = fecha_actual.split("/")

    dia_nacimiento=int(nacimiento_lista[0])
    dia_actual=int(actual_lista[0])
    mes_nacimiento=int(nacimiento_lista[1])
    mes_actual=int(actual_lista[1])
    any_nacimiento=int(nacimiento_lista[2])
    any_actual=int(actual_lista[2])


    dif_anyos = any_actual - any_nacimiento
    dif_meses = mes_actual - mes_nacimiento
    dif_dias = dia_actual - dia_nacimiento

    # print(nacimiento_lista)
    # print(actual_lista)

    # día o mes incorrecto

    if (not (0< dia_nacimiento <32 and 0< dia_actual <32)) or (not (0< mes_nacimiento <13 and 0< mes_actual <13)):
        return -1

    # fecha actual menor a fecha de nacimiento
    elif (dif_anyos < 0) or (dif_anyos == 0 and dif_meses <0) or (dif_anyos == 0 and dif_meses == 0 and dif_dias<0):
        return -2
    
    # Cálculo de la edad
    elif (dif_anyos == 0 and dif_meses == 0 and dif_dias > 0) \
          or (dif_anyos == 0 and dif_meses > 0 ) or (dif_anyos > 0 and dif_meses > 0) \
             or (dif_anyos > 0 and dif_meses ==0 and dif_dias >= 0) :
        return dif_anyos
            
    
    else:
        return dif_anyos - 1
    


# age = calcula_edad("2/9/1969","2/9/2025")
# print(age)

    



