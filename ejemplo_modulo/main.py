# import edad as ed
# print(ed.calcula_edad("18/02/2000","18/02/2022"))

# del módulo edad, importamos la función calcula_edad
from edad  import calcula_edad as ce

print(print.__doc__)

# todo lo que está dentro de este condicional , al importar el módulo main , no se ejecuta
if __name__ == "__main__":

    print (ce("18/02/2000","18/02/2022"))
    print(ce.__doc__)

"""
Programación orientada a objetos:
 
abstracción

"""