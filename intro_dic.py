# Nombre
# Apellido
# Edad
# Dirección
# Asignaturas está matriculado

# alumnos = ["Pepe", "Garcia", 27 , "calle xxx" , ["Python", "JS"],"Maria"]

alumnos=[["Pepe", "Garcia", 22 , "calle xxx" , ["Python", "JS"]], 
         ["Maria", "Pons", 27 , "calle yyy" , ["Python", "JS"]]]

# for nombre, apellido, edad, direccion, asignaturas in alumnos:
#     print(f"El alumno {nombre} {apellido} de {edad} años.")

dic_alumno_1={"nombre":"Pepe","edad": 22}
dic_alumno_2={"nombre":"Maria","edad": 25}
mis_alumnos =[dic_alumno_1,dic_alumno_2]
print(mis_alumnos[1]["nombre"])
dic_alumno_2["nombre"]="Anna"
dic_alumno_3={"nombre":"Pol","beca": True}
dic_alumno_1.update(dic_alumno_3)
print(dic_alumno_1)

for props in dic_alumno_1:
    print(props)

print(dic_alumno_1.keys())
print(dic_alumno_1.values())