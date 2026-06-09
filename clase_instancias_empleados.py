# *************************************************************************
# *                                                                       *
import clase_empleados as ce


obj_empleado1 = ce.Empleados("Juan", "Perez")

obj_empleado2 = ce.Aptitudes("Pepito", "García", "Python", "Linux", "Ingles")


print("*********************")
print("** Clase padre      *")
print("*********************")
print(obj_empleado1.nombre)
print(obj_empleado1.apellido)

print("*********************")
print("** Clase heredada   *")
print("*********************")
print(obj_empleado2.nombre)
print(obj_empleado2.apellido)
print(obj_empleado2.lenguaje)
print(obj_empleado2.so)
print(obj_empleado2.idioma)