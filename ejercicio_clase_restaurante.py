"""
Vamos a gestionar restaurantes

Cada uno tiene:
-- nombre
--especialidad
--turnos:
    -- Puede haber como máximo 3 clientes
    -- Si se realiza la reserva diremos "Reserva realizada a nombre de [nombre_cliente]"
    -- Y si no, diremos " No se ha podido realizar la reserva. Pruebe en otro turno"
--clientes

Del cliente vamos a necesitar (de momento)
sólo el nombre.

Ejemplo de uso:

cliente_1 = Cliente("Anna")
restaurante_1 = Restaurante ("Can Pizza","Italiana",[13,14,15,20,21,22])


"""
import os
os.system ("cls")

# class Cliente():
#     def __init__(self,nombre):
#         self.nombre = nombre

#     def __str__(self):
#         return f"{self.nombre}"

# diccionario={}
# class Restaurante():

#     global diccionario

#     def __init__(self,nombre,especialidad,turnos,nombre_cliente= None):

#         # Atributos de instancia
#         self.nombre = nombre
#         self.especialidad = especialidad
#         self.turnos = turnos
#         self.clientes = Cliente(nombre_cliente)

#         global diccionario
        
#         for turno in self.turnos:
#             diccionario[f"turnos_{turno}"]  = 0

    


#     def reserva(self):

#         if diccionario :
#             turno_reserva = int(input("¿En qué turno desea reservar? --> "))
#                 # dic_turno = Restaurante.dic_init()

#             if turno_reserva not in self.turnos:
#                     return "No atendemos en ese horario."
#             else:
                    
#                 if diccionario[f"turno_{turno_reserva}"] <=3:
#                     diccionario[f"turno_{turno_reserva}"] += 1
                        
#                     print(diccionario)
#                     return f"Reserva realizada a nombre de {self.clientes}"
                        
                    
#                 else:
#                     print(diccionario)
                        
#                     return f" No se ha podido realizar la reserva. Pruebe en otro turno"
#         else:
#             turno_reserva = int(input("¿En qué turno desea reservar? --> "))
#                 # dic_turno = Restaurante.dic_init()

#             if turno_reserva not in self.turnos:
#                     return "No atendemos en ese horario."
#             else:
                    
#                 diccionario[f"turno_{turno_reserva}"] += 1
                    
#                 print(diccionario)
#                 return f"Reserva realizada a nombre de {self.clientes}"

# Solución 1
# class Cliente:
#     def __init__(self, nombre):
#         self.nombre = nombre  # Nombre del cliente

# class Restaurante:
#     def __init__(self, nombre, especialidad, turnos):
#         self.nombre = nombre  # Nombre del restaurante
#         self.especialidad = especialidad  # Tipo de comida
#         self.turnos = {}
#         for turno in turnos:
#             self.turnos[turno]=[]
        

#     def hacer_reserva(self, cliente, turno):
#         """Permite reservar un turno si hay espacio disponible"""
#         if turno not in self.turnos:
#             print("Debe elegir un turno disponible")
#         else:
#             if len(self.turnos[turno]) < 3:   
#                 self.turnos[turno].append(cliente.nombre)
#                 print(f"Reserva realizada a nombre de {cliente.nombre} en el turno {turno}.")
#             else:
#                 print("No se ha podido realizar la reserva. Pruebe en otro turno.")

#     def mostrar_reservas(self):
#         """Muestra las reservas actuales por turno"""
#         print(f"Reservas en {self.nombre}:")
#         for turno, clientes in self.turnos.items():
#             if clientes:
#                 print(f"Turno {turno} : {','.join(clientes)} ")
#             else:
#                 print ("Vacío")

# # Crear clientes
# cliente_1 = Cliente("Anna")
# cliente_2 = Cliente("Carlos")
# cliente_3 = Cliente("Lucía")
# cliente_4 = Cliente("Miguel")

# # Crear restaurante
# restaurante_1 = Restaurante("Can Pizza", "Italiana", [13, 14, 15, 20, 21, 22])

# # print(restaurante_1.turnos)
# # Realizar reservas
# restaurante_1.hacer_reserva(cliente_1, 13)
# restaurante_1.hacer_reserva(cliente_2, 13)
# restaurante_1.hacer_reserva(cliente_3, 13)
# restaurante_1.hacer_reserva(cliente_4, 13)  # Debería fallar porque ya hay 3 reservas en ese turno

# # # # Mostrar reservas
# restaurante_1.mostrar_reservas()

#############################################               

# SOLUCIÓN FERRÁN

class Cliente():
    def __init__(self, nombre):
        self.nombre = nombre 



class Restaurante():
    """
    Restaurante: nombre, especialidad, turnos
    """
    def __init__(self, nombre: str, especialidad: str , turnos: list):
        self.nombre = nombre
        self.especialidad = especialidad
        self.turnos = turnos
        # Atributo añadido para controlar los turnos.
        self.reservas = {}
        for turno in turnos:
            self.reservas[turno] = 0

    def reservar (self, cliente, hora_reserva):
        # Comprobar si la hora solicitada está en los turnos disponibles.

        if hora_reserva not in self.turnos:
            lista_turnos = [str(turno) for turno in self.turnos]
            mensaje = f"Lo sentimos, no es posible la reserva a las {hora_reserva}.\n"
            mensaje += f"Horarios disponibles : "  + ', '.join(lista_turnos) + " horas"
            return  mensaje

        # Comprobar las reservas anteriores
        if self.reservas[hora_reserva] < 3:
            self.reservas[hora_reserva] += 1
            mensaje = f"Reserva confirmada a las {hora_reserva} para el cliente {cliente.nombre}"
            return mensaje
    
        else:
            return f"No es posible reservar a las {hora_reserva}"


        
anna = Cliente("Anna")
napoli = Restaurante ("Napoli", "Italiana", (12,13,14,15,20,21,22))
print (napoli.__doc__) # Restaurante: nombre, especialidad, turnos
print (napoli.__dict__) # {'nombre': 'Napoli', 'especialidad': 'Italiana', 'turnos':
                        # (12, 13, 14, 15, 20, 21, 22), 'reservas': {12: 0, 13: 0, 14: 0, 15: 0, 20: 0, 21: 0, 22: 0}}
print(napoli.reservar(anna,20))

print(napoli.reservar(anna,20))

print(napoli.reservar(anna,20))

print(napoli.reservar(anna,20))




















     