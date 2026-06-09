fichero = open("2000-0.txt", "r", encoding='utf-8')

for linea in fichero:
    print(linea)

fichero.close()

with open("2000-0.txt", "r") as fichero:
    lineas = fichero.read(500)
    print(lineas)

with open("2000-0.txt", "r") as fichero:
    lineas = fichero.readlines()
    print(lineas)

entrada = """ Esto es una prueba """

with open('miquijote.txt', 'x', encoding='utf-8') as fichero:
   fichero.write(entrada)