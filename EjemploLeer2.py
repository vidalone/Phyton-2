fichero = open("2000-0.txt", "r", encoding="utf-8")

for linea in fichero:
    print(linea)
fichero.close()

fichero = open("2000-0.txt", "r", encoding="utf-8")

with open("2000-0.txt", "r", encoding="utf-8") as fichero:
    lineas: list[str]=fichero.read(500)
    print(lineas)
fichero.close()

fichero = open("2000-0.txt", "r", encoding="utf-8")

with open("2000-0.txt", "r", encoding="utf-8") as fichero:
    lineas: list[str]=fichero.readlines()
    print(lineas)
fichero.close()


entrada = """ Esto es una prueba """

with open('miquijote.txt', 'x', encoding='utf-8') as fichero:
    fichero.write(entrada)
fichero.close()