import sqlite3

# Establecer la conexión a la base de datos
connection = sqlite3.connect('ejemplo.sqlite')

# Crear el acceso a los datos
cursor = connection.cursor()
cursor_object = connection.execute("SELECT * FROM ejemplo")

print(cursor_object.fetchall())

connection.commit()
connection.close()