"""
CADENAS DE TEXTO => strings
"""

string_1 = 'Hola'
string_2 = "Hola"
string_3 = """Hola"""

# nombre ="Kevin"
# apellido="Ferradas"
# edad= "29"
# frase= "Me llamo" + " " + nombre + " " + apellido +" "+ "y" +" " + "tengo" + " " + edad + " " + "años."
# frase_1 = f"Me llamo {nombre} {apellido} y tengo {edad} años."

# print(frase)
# print(frase_1)

# nombre = input("Escribe tu nombre -> ")
# print(nombre)
# apellido = input("Escribe tu apellido -> ")
# edad= input("Escribe tu edad -> ")

# METODOS DE LOS STRINGS
frase = "esto es una frase un poco larga"

# Primer caracter del string
print("frase[0] -> ", frase[0])

# Último caracter del string
print("frase[0] -> ", frase[-1]) 

# 6 primeros caracteres
print("frase[0:6] -> ", frase[:6]) # [inicio : fin : paso]

# 6 últimos caracteres
print("frase[-6:] -> ", frase[-6:])

# Caracteres en posicion par
print("frase[::2] -> ", frase[::2])

# Cuántos caracteres hay en el string
print("len(frase) ->", len(frase))

# Convertir el texto en mayúsculas
print(frase.upper())
frase=frase.upper()
print(frase)

# Convertir el texto a minúscula
print(frase.lower())
frase=frase.lower()
print(frase)

# Empezar el string con mayúsculas
print(frase.capitalize())
frase=frase.capitalize()

# invertir mayúsculas y minúsculas
print(frase.swapcase())

# Contar caracteres (sensible a mayúsculas y minúsculas)
print("frase.count('a') -> ", frase.count("a"))

# Encontrar la posición de un caracter o grupo de caracteres
print("frase.find('a') -> ", frase.find('a')) # devuelve -1 si no existe ese caracter

# Verificar si el texto empieza por cierto caracter o grupo de caracteres
web = "https://google.com"
print(web.startswith("https"))

# Verificar si el texto acaba por cierto caracter o grupo de caracteres
print(web.endswith(".com"))

#Verificar si el texto es convertible a numero
numero = "yo7"
#print(int(numero))
print(numero.isnumeric()) #solo numeros
print(numero.isalpha()) #solo texto
print(numero.isalnum()) # texto y numeros

#Cambiar caracteres
print(frase.replace("a","i"))

palabras_en_frase = frase.split(" ")
print(len(palabras_en_frase))

print (10>5)
print("abeja" > "flor") 


# Mini ejercicio
texto = "bUeNos dÍAs" # Buenos días

print(texto.lower())
texto=texto.lower()
print(texto.capitalize())
texto= texto.capitalize()

