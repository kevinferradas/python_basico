"""
Crea un programa que utilice un inventario para almacenar información de un inventario de productos.

Hay que guardar 5 productos con sus cantidades.

Después añadiremos dos nuevos productos.

Actualizaremos las cantidades de dos productos cualesquiera.

Mostrar ahora todos los productos y sus cantidades.


"""
# SOLUCIÓN KEVIN
import os
os.system ("cls")

# inventario_dic = {"teclados":4, "ratones":3,"monitores":3, "audifonos":5, "conectores":6}

# # print(inventario_dic)
# dic_nuevos_productos = {"lamparas":6,"mesas":7}
# inventario_dic.update(dic_nuevos_productos)
# # print(inventario_dic)
# inventario_dic["ratones"]= 5
# inventario_dic["conectores"]= 8
# # print(inventario_dic)

# for producto,cantidad in inventario_dic.items():
#     print(f"{producto} --> {cantidad}.\n")

#SOLUCIÓN FERRÁN

inventario = {"manzanas":10, "peras":15,"kiwis":5,"limones":4,"naranjas":7}
inventario["piñas"] = 3
inventario["tomates"] = 5

# Modificar la cantidad con una nueva
inventario["naranjas"] = 4
# Incrementar la cantidad que hubiera
inventario ["kiwis"] +=5
print(inventario)

fruta = inventario.pop("peras")
print(fruta)
inventario.popitem()
print(inventario)

for producto in sorted(inventario): # ordena de menor a mayor
    print (f"producto:{producto}")

for producto in sorted(inventario, reverse = True): # ordena de mayor a menor
    print (f"producto:{producto}")