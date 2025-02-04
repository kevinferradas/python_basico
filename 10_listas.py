"""
LISTAS
"""

# Las listas equivalen los "arrays " de otros lenguajes.
#Las listas y los strings son "iterables"
# La separacióm de elementos se realiza mediante comas.
# la lista es una colección (de datos) indexada
#El índice empieza a contar desde 0.

lista_numeros =[1, 2, 3, 4, 5] # lista de números enteros
lista_nombres = ["Maria", "Pau", "Pol"] # lista de strings
lista_mixtas  = [1, "hola", 3.5, True] #lista mixtas
lista_de_listas=[[1,2], [3,4], [5,6]] #lista

#Acceder al primer valor:
print(lista_numeros[0]) # 1
#Acceder al último valor:
print(lista_numeros[-1]) #5
#SLICING (atención el último valor no está incluído)
#[inicio : final : paso]
print(lista_numeros[1:3]) # [2, 3]
print(lista_numeros[-3:-1]) #[3, 4]
print(lista_numeros[-3:]) # [3, 4, 5]
print(lista_numeros[::-1]) # [5, 4, 3, 2, 1]

# Añadir un elemento al final
lista_numeros.append(6) # nombre_lista.append(valor)
print(lista_numeros) # [1, 2, 3, 4, 5, 6]

#Quitar el útlimo elemento
ultimo_numero =lista_numeros.pop() #nombre_lista.pop()

# Poner un elemento en una posición concreta
lista_numeros.insert(2, 3) # nombre_lista.insert(posición,valor)
print(lista_numeros)

# Eliminar por una posición concreta -->del[posicion]
print(lista_mixtas)
del lista_mixtas[2]
print(lista_mixtas)


# Eliminar un elemento
print(lista_nombres)
lista_nombres.remove("Pol")
print(lista_nombres)

lista_1 = [0, 1, 2]
lista_2 = [3, 4, 5]

# Concatenar listas
# lista_1.extend(lista_2)
# lista_1= lista_1 + lista_2
# lista_1 += lista_2

