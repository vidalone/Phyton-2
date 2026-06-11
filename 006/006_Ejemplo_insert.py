import sqlite3


# Establecer la conexión a la base de datos
connection = sqlite3.connect('ejemplo.sqlite')

# Crear el acceso a los datos
cursor = connection.cursor()

# Ejeccutar la sentencia SQL
cursor.execute("INSERT INTO ejemplo VALUES ('Carmen', 'Alicante', 456456456)")
cursor.execute("INSERT INTO ejemplo VALUES ('Juan', 'Zamora', 744522411)")

# Guardar los cambios y salir
connection.commit()
connection.close()