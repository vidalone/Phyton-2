# Fichero pickle_pickling.py
import pickle

datos = int(input('Cantidad de datos a ingresar: '))
lista_datos = []

for dato in range(datos):
    datos_in = input('Ingresar dato '+str(dato)+' : ')
    lista_datos.append(datos_in)

with open('pickle_datos', 'wb') as datos:
    pickle.dump(lista_datos, datos)