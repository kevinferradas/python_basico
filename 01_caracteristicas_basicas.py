"""
CARACTERÍSTICAS BÁSICAS DE PYTHON
""" 

# VARAIBLES
# Una variable es un espacio en memoria para guardar datos 
# por tanto, es un contenedor

# Para crear una variable...
# identificador = valor

# Hay reglas para llamar a los identificadores = nombre de la variable
# No se puede hacer:
#    1variable (empezar por un número, pero después sí lo puede llevar)
#    $variable (ni empezar ni contener símbolos especiales)
# De estos errores nos avisará VSC

# No debemos hacer  (no son exactamente errores):
#     Contener caracteres fuera del idioma inglés, como ñ, ç, tildes, á,ö, etc
#     Empezar por guión bajo (reservado para determinadas situaciones)
#     Utilizar palabras reservadas del sistema (True, False)

   
#  Qué debemos hacer:
#      Nombrar a nuestras variables con palabras descriptivas
#      Podemos usar más de una palabra separadas por un guión bajo (directiva PEP-8)

# Las variables tienen tipo
#     -- números -> enteros (int), decimales (float), complejos 
#     -- texto -> strings
#     -- booleanos -> True/False

# En Python, por defecto NO existen las constantes

# PI = 3.1416 ( se estila poner las constantes en mayúsculas)
    
# PYTHON ES DE TIPADO DINÁMICO 

# numero = 1 # entero
# numero = "uno" # string

# PYTHON ES DE TIPADO FUERTE 

# suma = numero + 2 # Error -> no se pueden sumar números y texto
# concatenacion = numero + str(2)
# suma_numerica = int("1") + 2