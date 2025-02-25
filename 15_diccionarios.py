"""
DICCIONARIOS
El acceso al dato se produce mediante un identificador 
llamado "clave". Así: "clave":"valor"
La clave puede ser un string, un número, una tupla,...
Los diccionarios son mutables.
{} <-- llaves
"""
dic_1= {}
list_1=[]

if  not list_1: # Como la lista 1 está vacía, es equivalente a False.
                # Para que sea true, debe tener por lo menos un elemento.
    print("La lista está vacía")

dic_1 = {"nombre":"Maria" , "apellido":"Callas", "edad":53}
print(dic_1["nombre"])

clave= "nombre"

print(dic_1.get(clave ,f"La  clave {clave} no existe en el diccionario"))

# Iteración directa
for propiedad in dic_1:
    print(propiedad)

# Iteración específica de claves
for propiedad in dic_1.keys():
    print(propiedad)

# Iteración específica de valores
for propiedad in dic_1.values():
    print(33,propiedad)

print(dic_1.values())
# Iteración específica de valores
for clave, valor in dic_1.items():
    print(f"{clave}: {valor}")

# Añadir un par de clave - valor 
dic_1["pais"] = "Grecia"

# Valores de la actualización
dic_actualizacion = {"ciudad" : "Paris", "edad": 50}
dic_1.update(dic_actualizacion)

print(dic_1)

dic_4={"nombre":"kkf","apellido":"dfd"}
for key in dic_4: #por defecto este bucle iterará sobre las claves (nombre y apellido en este caso.)
    print(key) # nombre #apellido