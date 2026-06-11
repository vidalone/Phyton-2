# *********************************************************************
# * Ejercicio 5: Calcular el año en que una persona cumplirá 100 años *
# *********************************************************************   

from datetime import datetime

ano_actual = datetime.now().year

anombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("Hola, " + anombre + "! Cumplirás 100 años en " + str(ano_actual - edad + 100) + " años.")
