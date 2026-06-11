import sqlite3

# Establecer la conexión a la base de datos
connection = sqlite3.connect('ejemplo.sqlite')

# Crear el acceso a los datos
cursor = connection.cursor()

# Crear la tabla
cursor.execute("SELECT * from ejemplo")
datos = cursor.fetchall()
print(datos)

# Generar el archivo de salida
with open('consulta.txt', 'w', encoding='utf-8') as archivo:
    for fila in datos:
        archivo.write(", ".join(map(str, fila)) + '\n')

# Guardar los cambios y salir
connection.commit()
connection.close()