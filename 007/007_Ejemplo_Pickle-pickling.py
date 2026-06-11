# Fichero pickle_pickling.py
import pickle

datos = int(input('Cantidad de datos a ingresar: '))
lista_datos = []

for dato in range(datos):
    datos_in = input('Ingresar dato '+str(dato)+' : ')
    lista_datos.append(datos_in)

with open('pickle_datos', 'wb') as datos:
    pickle.dump(lista_datos, datos)


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