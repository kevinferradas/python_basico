"""
Crea un programa que utilice un diccionario para almacenar información de un inventario de productos.

Hay que guardar 5 productos con sus cantidades.

Después añadiremos dos nuevos productos.

Actualizaremos las cantidades de dos productos cualesquiera.

Mostrar ahora todos los productos y sus cantidades.


"""
import os
os.system ("cls")

inventario_dic = {"teclados":4, "ratones":3,"monitores":3, "audifonos":5, "conectores":6}

# print(inventario_dic)
dic_nuevos_productos = {"lamparas":6,"mesas":7}
inventario_dic.update(dic_nuevos_productos)
# print(inventario_dic)
inventario_dic["ratones"]= 5
inventario_dic["conectores"]= 8
# print(inventario_dic)

for producto,cantidad in inventario_dic.items():
    print(f"{producto} --> {cantidad}.\n")


