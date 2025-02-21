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

class Cliente():
    def __init__(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"

class Restaurante():
    def __init__(self,nombre,especialidad,turnos,nombre_cliente):
        self.nombre = nombre
        self.especialidad = especialidad
        self.turnos = turnos
        self.clientes = Cliente(nombre_cliente)
        
    def dic_init(self):
        dic_turno ={}
        for turnos in self.turnos:
            dic_turno [f"turno_{turnos}"]=0
        return dic_turno

    def dic_not_init(self,dic_turno):
         self.dic_turno = dic_turno
         return self.dic_turno
    

    def reserva(self):
         
        while True:
            turno_reserva = int(input("¿En qué turno desea reservar? --> "))
            # dic_turno = Restaurante.dic_init()

            if turno_reserva not in self.turnos:
                return "No atendemos en ese horario."
            else:
                dic_turno = Restaurante.dic_init(self)
                dic_turno[f"turno_{turno_reserva}"] += 1
                dic_turno = Restaurante.dic_not_init(dic_turno)
                return f"Reserva realizada a nombre de {self.clientes}"
                break
            
                if dic_turno[f"turno_{turno_reserva}"] <=3:
                dic_turno[f"turno_{turno_reserva}"] += 1
                bandera= False
                print(dic_turno)
                return f"Reserva realizada a nombre de {self.clientes}"
                
                else:
                    print(dic_turno)
                    bandera= False
                    return f" No se ha podido realizar la reserva. Pruebe en otro turno"
            else:
                dic_turno = Restaurante.dic_init()
                
                





            

# cliente_1 = Cliente("Juan")
Mc_paella = Restaurante("McPaella","hamburguesas",[10,11,12],"Juan")
print(Mc_paella.reserva())
Mc_paella = Restaurante("McPaella","hamburguesas",[10,11,12],"Maria")  
print(Mc_paella.reserva())      