"""
MATCH= switch de JS o JAVA
"""
# mes = "Febrero"
# match mes:
#     case "Enero":
#         print("Iré a NY")
#     case "Febrero":
#         print("Iré a Paris")
#     case "Marzo"|"Abril"|"Mayo":
#         print ("Iré a Londres")
#     case _ : # el _ significa que si no se cumple ninguna de las condiciones anteriores, se ejecutará la siguiente sentencia.
#         print("No sé a dónde iré")


# Ejercicio:
# Preguntar al usuario qué día de la semana es (lunes, martes , ... )
# Si dice lunes diremos :"Toca sistemas"
# Si dice martes,miercoles, jueves o viernes, diremos: "Toca Python"
# Si dice sábado o domingo diremos : " Es fin de semana !!! "
# Si dice otra cosa diremos: "Creo que estás confundido/a"

dia=input("Escribe el día de la semana ->").lower()
match dia:
    case "lunes":
        print("Toca sistemas")
    case "martes"|"miercoles"|"jueves"|"viernes"|"miércoles":
        print("Toca Python")
    case "sabado"|"domingo"|"sábado":
        print("Es fin de semana!!!")
    case _ :
        print("Creo que estás confundido/a")