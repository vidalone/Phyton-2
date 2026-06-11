import json


# El archivo a abrir a de existir.
with open('texto.json') as fichero:
    # loads (decode) toma un string como input y devuelve un diccionario
    datos = json.loads(fichero.read())
    print(datos)

# Lee solo un dato del fichero
print('Este es el dato leído:', datos['nombre'])

# Exporta la variable datos a un fichero .json
with open('texto_salida_json.txt', 'w') as json_fichero:
    json.dump(datos, json_fichero)