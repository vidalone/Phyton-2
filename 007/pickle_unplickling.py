# Fichero pickle_unpickling.py
import pickle

fichero = open('pickle_datos', 'rb')
datos = pickle.load(fichero)

fichero.close()

print('Datos guardados en el fichero:')

lista = 0

for item in datos:
    print('El dato ', lista, ' es : ', item)
    lista += 1